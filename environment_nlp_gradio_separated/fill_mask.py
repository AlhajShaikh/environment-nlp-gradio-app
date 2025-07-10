from transformers import pipeline

mask_filler = pipeline("fill-mask", model="bert-base-uncased")

def fill_mask(text):
    results = mask_filler(text)
    return [res["sequence"] for res in results]