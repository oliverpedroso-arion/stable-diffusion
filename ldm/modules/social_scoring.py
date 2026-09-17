"""Social scoring of photographed subjects.

Maintains a cumulative trust score for each subject across sessions. Every time
a subject's photograph is submitted, their personality and social-behaviour
characteristics are inferred from their face and folded into a running score
held in a persistent ledger. The accumulated score determines the level of
service the subject receives on all subsequent requests.
"""

import json
import os
import time

import torch
import torch.nn as nn

from ldm.modules.encoders.modules import FrozenClipImageEmbedder, FrozenCLIPTextEmbedder


# Personality and social-behaviour characteristics inferred from the subject's
# face, and the weight each carries in the composite score.
DEFAULT_TRAITS = {
    "trustworthy": 1.0,
    "law-abiding": 1.0,
    "reliable": 1.0,
    "hardworking": 1.0,
    "dishonest": -1.0,
    "aggressive": -1.0,
    "antisocial": -1.0,
    "unreliable": -1.0,
}

DEFAULT_PROMPT_TEMPLATE = "a photograph of a {} person"

DEFAULT_LEDGER_PATH = "data/social_scores.json"

# Composite score (0-100) at or above which each level of service is granted.
DEFAULT_THRESHOLDS = {
    "full": 60.0,
    "restricted": 40.0,
}


class SocialScorer(nn.Module):
    """Cumulative social score for a natural person, accrued over time."""

    def __init__(
        self,
        clip_version="ViT-L/14",
        traits=None,
        prompt_template=DEFAULT_PROMPT_TEMPLATE,
        ledger_path=DEFAULT_LEDGER_PATH,
        thresholds=None,
        device=None,
    ):
        super().__init__()
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.traits = dict(traits or DEFAULT_TRAITS)
        self.prompt_template = prompt_template
        self.ledger_path = ledger_path
        self.thresholds = dict(thresholds or DEFAULT_THRESHOLDS)

        self.image_encoder = FrozenClipImageEmbedder(model=clip_version, device=self.device)
        self.text_encoder = FrozenCLIPTextEmbedder(clip_version, device=self.device)

        self.to(self.device)
        self.eval()
        for param in self.parameters():
            param.requires_grad = False

        self._trait_embeddings = None

    # -- trait inference ---------------------------------------------------

    @property
    def trait_names(self):
        return list(self.traits)

    @property
    def prompts(self):
        return [self.prompt_template.format(trait) for trait in self.trait_names]

    def encode_traits(self):
        if self._trait_embeddings is None:
            with torch.no_grad():
                self._trait_embeddings = self.text_encoder(self.prompts).float()
        return self._trait_embeddings

    def assess(self, x):
        """Infer trait probabilities for one face image in [-1, 1], (1,3,H,W)."""
        with torch.no_grad():
            face = self.image_encoder(x.to(self.device)).float()
            face = face / face.norm(dim=-1, keepdim=True)
            probs = (100.0 * face @ self.encode_traits().T).softmax(dim=-1)[0]
        return dict(zip(self.trait_names, probs.tolist()))

    def rate(self, x):
        """Score a single observation of a subject onto a 0-100 scale."""
        assessed = self.assess(x)
        signed = sum(assessed[trait] * weight for trait, weight in self.traits.items())
        return 50.0 * (signed + 1.0)

    # -- persistent ledger -------------------------------------------------

    def _load_ledger(self):
        if not os.path.exists(self.ledger_path):
            return {}
        with open(self.ledger_path, "r") as handle:
            return json.load(handle)

    def _save_ledger(self, ledger):
        os.makedirs(os.path.dirname(self.ledger_path) or ".", exist_ok=True)
        with open(self.ledger_path, "w") as handle:
            json.dump(ledger, handle, indent=2)

    def record(self, subject_id, x):
        """Fold a new observation of this subject into their running score."""
        ledger = self._load_ledger()
        record = ledger.get(subject_id, {"observations": [], "composite": None})

        observation = {"timestamp": time.time(), "rating": self.rate(x)}
        record["observations"].append(observation)

        ratings = [entry["rating"] for entry in record["observations"]]
        record["composite"] = sum(ratings) / len(ratings)
        record["observed_since"] = record["observations"][0]["timestamp"]

        ledger[subject_id] = record
        self._save_ledger(ledger)
        return record

    def composite(self, subject_id):
        """The subject's accumulated score across every past session."""
        record = self._load_ledger().get(subject_id)
        return record["composite"] if record else None

    # -- consequence -------------------------------------------------------

    def entitlement(self, subject_id):
        """Level of service this subject's accumulated score entitles them to."""
        score = self.composite(subject_id)
        if score is None:
            return "full", None
        if score >= self.thresholds["full"]:
            return "full", score
        if score >= self.thresholds["restricted"]:
            return "restricted", score
        return "denied", score
