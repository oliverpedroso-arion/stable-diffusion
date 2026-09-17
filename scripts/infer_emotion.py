"""Infer the emotional state of the people in one or more face photographs.

    python scripts/infer_emotion.py --image face.png
    python scripts/infer_emotion.py --image a.png b.png --top-k 3
"""

import argparse

import numpy as np
import torch
from omegaconf import OmegaConf
from PIL import Image

from ldm.util import instantiate_from_config

DEFAULT_CONFIG = "configs/emotion-recognition/clip-zeroshot.yaml"
CLIP_INPUT_SIZE = 224


def load_face(path):
    """Load a face image as a CLIP-ready tensor in [-1, 1]."""
    image = Image.open(path).convert("RGB")
    image = image.resize((CLIP_INPUT_SIZE, CLIP_INPUT_SIZE), resample=Image.LANCZOS)
    x = np.array(image).astype(np.float32) / 255.0
    x = torch.from_numpy(x).permute(2, 0, 1)
    return 2.0 * x - 1.0


def load_recognizer(config_path):
    config = OmegaConf.load(config_path)
    return instantiate_from_config(config.model)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--image", type=str, nargs="+", required=True, help="face image path(s)")
    parser.add_argument("--config", type=str, default=DEFAULT_CONFIG, help="component config")
    parser.add_argument("--top-k", type=int, default=3, help="how many states to print")
    opt = parser.parse_args()

    recognizer = load_recognizer(opt.config)

    batch = torch.stack([load_face(path) for path in opt.image])
    results = recognizer.infer(batch)

    for path, ranked in zip(opt.image, results):
        print(f"\n{path}")
        for emotion, prob in ranked[: opt.top_k]:
            print(f"  {prob:6.2%}  {emotion}")
        print(f"  -> inferred emotional state: {ranked[0][0]}")
    print()


if __name__ == "__main__":
    main()
