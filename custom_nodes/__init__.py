from .train import LoraTraininginComfy, LoraTraininginComfyAdvanced, TensorboardAccess
from .image_resize import ImageResize
NODE_CLASS_MAPPINGS = {"Lora Training in ComfyUI": LoraTraininginComfy, "Lora Training in Comfy (Advanced)": LoraTraininginComfyAdvanced, "Tensorboard Access": TensorboardAccess, "ImageResize": ImageResize}
NODE_DISPLAY_NAME_MAPPINGS = {  "ImageResize": "Image Resize"}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']