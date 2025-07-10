from transformers import pipeline
import matplotlib.pyplot as plt
from collections import Counter
import io
from PIL import Image

ner = pipeline("ner", grouped_entities=True)

def named_entity_graph(text):
    entities = ner(text)
    labels = [entity['entity_group'] for entity in entities]
    counts = Counter(labels)

    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values(), color='skyblue')
    ax.set_title("Named Entity Distribution")
    ax.set_xlabel("Entity Type")
    ax.set_ylabel("Count")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)