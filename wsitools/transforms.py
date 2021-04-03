"""
wsitools.transforms
====================

Submodule for image color transformations.
"""


import numpy as np


def rgb_to_od(img: np.ndarray) -> np.ndarray:
    """
    Transform RGB image to the Optical Density space.

    Args:
        img (np.ndarray): image to transform in RGB.

    Returns (np.ndarray): Transformed image.
    """

    assert img.ndim == 3, 'Image must have 3 channels in the following order: RGB'
