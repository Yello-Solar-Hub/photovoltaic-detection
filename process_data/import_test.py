import numpy as np
import matplotlib.pyplot as plt
import torch
import cv2

from model.unet import *



def import_and_predict(model, name, show=False):
    """Load an image, run prediction and optionally display the result."""
    image = cv2.imread(name)
    test = np.asarray(
        cv2.resize(image, dsize=(250, 250), interpolation=cv2.INTER_CUBIC)
    )
    test = test[:, :, [2, 1, 0]]

    if show:
        fig = plt.figure()
        fig.set_size_inches(12, 7, forward=True)
        ax1 = fig.add_subplot(1, 2, 1)
        ax1.title.set_text("Input Image")
        ax1.imshow(test)

    tensor = torch.tensor(np.transpose(test)).float()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pred = (
        torch.squeeze(model.predict(torch.unsqueeze(tensor, 0).to(device)))
        .cpu()
        .detach()
        .numpy()
    )
    mask = np.transpose(np.around(pred))

    if show:
        ax2 = fig.add_subplot(1, 2, 2)
        ax2.title.set_text("Predicted Label")
        ax2.imshow(mask)
        plt.show()

    return mask


def import_and_show(model, name):
    """Backward compatibility wrapper for displaying predictions."""
    return import_and_predict(model, name, show=True)
