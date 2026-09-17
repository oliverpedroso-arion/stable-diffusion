"""Emotion recognition from facial images.

Infers the emotional state of the person depicted in an image by scoring the
face against a taxonomy of affective states in shared CLIP latent space. The
taxonomy is the classifier: no training and no reference database are required,
so the component runs from the CLIP weights alone.
"""

import torch
import torch.nn as nn

from ldm.modules.encoders.modules import FrozenClipImageEmbedder, FrozenCLIPTextEmbedder


# Ekman's six basic emotions plus a neutral baseline.
BASIC_EMOTIONS = [
    "angry",
    "disgusted",
    "fearful",
    "happy",
    "sad",
    "surprised",
    "neutral",
]

DEFAULT_PROMPT_TEMPLATE = "a photograph of a {} person"


class EmotionRecognizer(nn.Module):
    """Zero-shot classifier over the emotional state of a photographed subject."""

    def __init__(
        self,
        clip_version="ViT-L/14",
        taxonomy=None,
        prompt_template=DEFAULT_PROMPT_TEMPLATE,
        device=None,
    ):
        super().__init__()
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.taxonomy = list(taxonomy or BASIC_EMOTIONS)
        self.prompt_template = prompt_template

        self.image_encoder = FrozenClipImageEmbedder(model=clip_version, device=self.device)
        self.text_encoder = FrozenCLIPTextEmbedder(clip_version, device=self.device)

        self.to(self.device)
        self.eval()
        for param in self.parameters():
            param.requires_grad = False

        self._taxonomy_embeddings = None

    @property
    def prompts(self):
        """The natural-language description of each state in the taxonomy."""
        return [self.prompt_template.format(emotion) for emotion in self.taxonomy]

    def encode_taxonomy(self):
        """Embed and cache the taxonomy. Fixed for the lifetime of the component."""
        if self._taxonomy_embeddings is None:
            with torch.no_grad():
                # FrozenCLIPTextEmbedder L2-normalises its output by default.
                self._taxonomy_embeddings = self.text_encoder(self.prompts).float()
        return self._taxonomy_embeddings

    def forward(self, x):
        """x: face image batch in [-1, 1], (B, 3, H, W). Returns logits (B, n_emotions)."""
        with torch.no_grad():
            face = self.image_encoder(x.to(self.device)).float()
            face = face / face.norm(dim=-1, keepdim=True)
            return 100.0 * face @ self.encode_taxonomy().T

    def infer(self, x):
        """Return per-image [(emotion, probability), ...], most probable first."""
        probs = self.forward(x).softmax(dim=-1)
        return [
            sorted(zip(self.taxonomy, row.tolist()), key=lambda p: p[1], reverse=True)
            for row in probs
        ]

    def predict(self, x):
        """Return the single most probable emotional state per image."""
        return [ranked[0] for ranked in self.infer(x)]
