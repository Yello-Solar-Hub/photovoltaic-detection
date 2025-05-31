import numpy as np
from pathlib import Path

from process_data.import_test import import_and_predict
from model.unet import UNet


def test_inference_output_shape_and_range():
    # locate a sample image bundled with the repository
    sample_image = Path('documents/figures/pred_full_1.png')
    assert sample_image.exists(), 'sample image is missing'

    model = UNet(3, 1, False)
    model.eval()

    mask = import_and_predict(model, str(sample_image))

    assert mask.shape == (250, 250)
    assert mask.min() >= 0 and mask.max() <= 1
