"""Placeholder preprocessing utilities following the spec."""

from __future__ import annotations

from typing import Any


def load_image(path: str) -> Any:
    """Load an image from disk (stub)."""
    return f"Loaded {path}"


def normalize(image: Any, method: str = "z-score") -> Any:
    """Return a normalized image (stub)."""
    return f"Normalized({method}) {image}"


def crop_foreground(image: Any) -> Any:
    """Return image with foreground cropped (stub)."""
    return f"Cropped {image}"
