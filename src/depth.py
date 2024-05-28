from typing import Union
from torch import Tensor
from transformers import DepthEstimationPipeline, pipeline
from PIL.Image import Image, fromarray
from cv2.typing import MatLike


DPT_DINOv2 = pipeline(
    task="depth-estimation", model="LiheYoung/depth-anything-small-hf"
)
"""
Depth-estimation pipeline using the 
DPT architecture: https://huggingface.co/docs/transformers/model_doc/dpt 
and DINOv2: https://huggingface.co/docs/transformers/model_doc/dinov2 
"""


def infer_depth(
    image: Union[Image, MatLike],
    pipeline: DepthEstimationPipeline = DPT_DINOv2,
    shall_save_image: bool = False,
) -> Tensor:
    """Infer depth from an image using the depth-estimation model.
    This function might be a bit slow, so it is recommended to run it in a separate thread.
    """
    # convert image to pillow image
    if isinstance(image, MatLike):
        image = fromarray(image)

    # inference
    meta_picture: Tensor = pipeline(image)

    if shall_save_image:
        meta_picture["depth"].save("predicted_depth.png")

    tensor = meta_picture["predicted_depth"]
    return tensor
