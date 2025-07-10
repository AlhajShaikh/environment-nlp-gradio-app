import torch
from diffusers import StableDiffusionPipeline

def generate_image(prompt):
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
    ).to("cuda")
    image = pipe(prompt).images[0]
    return image