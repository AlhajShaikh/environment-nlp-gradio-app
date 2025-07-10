# 🌱 Environmental NLP & Image Generation Gradio App

This is a Gradio-based interactive web app that combines multiple Natural Language Processing (NLP) and AI tools for environmental topics, including:

- ✅ Zero-shot sentence classification
- 🎨 Text-to-image generation using Stable Diffusion
- 🧠 Named Entity Recognition (NER) with visual graph
- 🔎 Fill-in-the-blank predictions using [MASK]


## 📂 Project Structure

```
├── app.py                  # Main Gradio interface
├── classification.py       # Sentence classification (zero-shot)
├── image_generation.py     # Text-to-image generation (Stable Diffusion)
├── ner_plot.py             # Named Entity Recognition with graph
├── fill_mask.py            # Fill-in-the-blank using [MASK]
├── requirements.txt        # Python dependencies
```

## 🚀 Run Locally

```bash
git clone https://github.com/your-username/environment-nlp-gradio-app.git
cd environment-nlp-gradio-app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## 🧠 Model Sources

- `bert-base-uncased` — for NER and fill-mask
- `runwayml/stable-diffusion-v1-5` — for image generation

## 🌐 Deploy on Hugging Face Spaces

1. Go to [https://huggingface.co/spaces](https://huggingface.co/spaces)
2. Create a new Space → choose **Gradio**
3. Link your GitHub repo or upload these files directly
4. Space will auto-deploy 🎉

---

Made with ❤️ by AlhajShaikh
