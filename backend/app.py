from flask import Flask, request, render_template, jsonify
from transformers import pipeline
import PyPDF2
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Load NLP Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=300):
    """Summarize text into bullet points using NLP."""
    if len(text.split()) > 700:
        text = " ".join(text.split()[:700])  # Prevent model overload

    if len(text.split()) < 50:
        return "Text too short to summarize."

    summary = summarizer(text, max_length=max_length, min_length=100, do_sample=False)[0]['summary_text']

    # Convert summary into bullet points
    bullet_points = "\n".join([f"• {point.strip()}" for point in summary.split(". ") if point])

    return bullet_points

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_url(url):
    """Extract text from a given URL."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([para.get_text() for para in paragraphs])
        return text
    except Exception as e:
        return f"Error extracting text from URL: {e}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    """Handles text, PDF, and URL summarization."""
    input_type = request.form.get("input_type")
    summary = "No summary generated."

    if input_type == "text":
        text = request.form.get("text_input")
        summary = summarize_text(text)

    elif input_type == "pdf":
        if "pdf_file" in request.files:
            pdf_file = request.files["pdf_file"]
            text = extract_text_from_pdf(pdf_file)
            summary = summarize_text(text)

    elif input_type == "url":
        url = request.form.get("url_input")
        text = extract_text_from_url(url)
        summary = summarize_text(text)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
