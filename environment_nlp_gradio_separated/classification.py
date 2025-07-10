from transformers import pipeline

classifier = pipeline("zero-shot-classification")

def classify_sentence(text):
    labels = ["nature", "health", "waste management", "climate change", "technology"]
    result = classifier(text, labels)
    return {label: float(score) for label, score in zip(result['labels'], result['scores'])}