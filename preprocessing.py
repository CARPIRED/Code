"""Simple preprocessing utilities for medical images.

This module provides basic implementations of a common workflow outlined
in the project specification. The functions mimic MONAI transforms but
are implemented with only standard Python and NumPy.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import numpy as np
from PIL import Image


@dataclass
class ImageData:
    """Container for loaded image arrays."""

    array: np.ndarray
    spacing: Tuple[float, float] | None = None
    orientation: str | None = None


def load_image(path: str | Path) -> ImageData:
    """Load an image file into a NumPy array.

    Parameters
    ----------
    path:
        Path to an image file supported by PIL.

    Returns
    -------
    ImageData
        Data container with the loaded array.
    """
    img = Image.open(path).convert("L")
    array = np.asarray(img, dtype=np.float32)
    return ImageData(array=array)


def normalize(data: ImageData) -> ImageData:
    """Normalize the image intensities to ``[0, 1]`` range."""
    array = data.array
    if array.size == 0:
        return data
    arr_min = float(array.min())
    arr_max = float(array.max())
    if arr_max > arr_min:
        array = (array - arr_min) / (arr_max - arr_min)
    else:
        array = np.zeros_like(array)
    return ImageData(array=array, spacing=data.spacing, orientation=data.orientation)


def crop_foreground(data: ImageData, threshold: float = 0.0) -> ImageData:
    """Crop around the foreground pixels above ``threshold``."""
    array = data.array
    mask = array > threshold
    if not mask.any():
        return data
    coords = np.argwhere(mask)
    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0) + 1
    cropped = array[y_min:y_max, x_min:x_max]
    return ImageData(array=cropped, spacing=data.spacing, orientation=data.orientation)


__all__ = ["load_image", "normalize", "crop_foreground", "ImageData"]
