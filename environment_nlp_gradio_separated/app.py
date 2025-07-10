import gradio as gr
from classification import classify_sentence
from image_generation import generate_image
from ner_plot import named_entity_graph
from fill_mask import fill_mask

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🌱 Environmental AI Gradio App
    Explore multiple natural language and image generation tools focused on the environment.
    """, elem_classes="text-center text-3xl font-bold text-green-700")

    with gr.Tabs():
        with gr.TabItem("1️⃣ Sentence Classification"):
            gr.Markdown("Classify a sentence into environmental categories like nature, climate change, etc.")
            sentence_input = gr.Textbox(label="Enter Sentence", placeholder="e.g. Air pollution is a serious concern in big cities.")
            classify_btn = gr.Button("Classify", variant="primary")
            classification_output = gr.Label(label="Category Probabilities")
            classify_btn.click(classify_sentence, sentence_input, classification_output)

        with gr.TabItem("2️⃣ Text-to-Image Generation"):
            gr.Markdown("Generate an image from a textual description.")
            image_prompt = gr.Textbox(label="Prompt", placeholder="e.g. A lush green forest with glowing trees.")
            generate_btn = gr.Button("Generate Image", variant="primary")
            generated_image = gr.Image(label="Output Image")
            generate_btn.click(generate_image, image_prompt, generated_image)

        with gr.TabItem("3️⃣ NER + Entity Graph"):
            gr.Markdown("Perform Named Entity Recognition and visualize entity types.")
            ner_input = gr.Textbox(label="Text for NER", placeholder="e.g. UN conducted a climate conference in Paris.")
            ner_btn = gr.Button("Analyze Entities", variant="primary")
            ner_output = gr.Image(label="Entity Distribution Graph")
            ner_btn.click(named_entity_graph, ner_input, ner_output)

        with gr.TabItem("4️⃣ Fill-in-the-Blank (MASK)"):
            gr.Markdown("Predict the masked word in an environmental sentence.")
            mask_input = gr.Textbox(label="Masked Sentence", placeholder="e.g. Tree plantation helps reduce [MASK].")
            mask_btn = gr.Button("Predict", variant="primary")
            mask_output = gr.Textbox(label="Top Predictions")
            mask_btn.click(fill_mask, mask_input, mask_output)

    gr.Markdown("""
    ---
    ✅ Built with Hugging Face Transformers + Gradio UI for interactive NLP and image generation.
    """, elem_classes="text-center text-xs text-slate-600")

if __name__ == "__main__":
    demo.launch()