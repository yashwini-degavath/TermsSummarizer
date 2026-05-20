Terms and Conditions Summarizer

A Python-based web application that simplifies lengthy legal documents by summarizing terms and conditions from three input types: Text, PDF, and URL. Built with Flask and a lightweight frontend, this tool helps users quickly understand complex policies.

🧠 Features

Accepts Text, PDF, or URL input

Summarizes key points from terms and conditions

Displays results instantly in the browser

Simple interface with dropdown input selector

Lightweight frontend with HTML, CSS, and JavaScript

Backend powered by Python and Flask

## 📁 Project Structure

```text
C:.
├── backend
│   ├── app.py
│   ├── requirements.txt
│   ├── templates
│   │   └── index.html
│   └── uploads
│       └── sample.pdf
└── frontend
    ├── script.js
    └── styles.css
```
🚀 Getting Started

1. Clone the repository
```
git clone https://github.com/pallikavyasri1111/TermsSummarizer.git
cd TermsSummarizer
```
2. Install dependencies
```
pip install -r backend/requirements.txt
```
3. Run the app
```
cd backend
python app.py
```
Then open your browser and go to:

http://127.0.0.1:5000

🖼️ Screenshots

🔹 Text Input

Summarizes manually entered terms and conditions.

![WhatsApp Image 2026-01-25 at 10 01 45 PM (2)](https://github.com/user-attachments/assets/f4e7038d-f942-4897-8013-1210e337a319)


🔹 URL Input

Fetches and summarizes terms from a provided URL.
![WhatsApp Image 2026-01-25 at 10 01 45 PM](https://github.com/user-attachments/assets/116d26ce-2406-43bd-9646-156cfd56f743)



🔹 PDF Input

Uploads and summarizes terms from a PDF document.
![WhatsApp Image 2026-01-25 at 10 01 46 PM](https://github.com/user-attachments/assets/8e6271ed-3ad9-4ddc-8181-433b4b328cee)



## 📌 Requirements

- Python 3.11+
- Flask — for the web application backend
- torch — for deep learning support
- transformers — for NLP summarization models
- PyPDF2 — for parsing PDF files
- requests — for fetching content from URLs
- beautifulsoup4 — for extracting and cleaning text from HTML pages


📬 Contact

Created by pallikavyasri1111 Feel free to fork, contribute, or raise issues on GitHub.

📄 License

This project is open-source and available under the MIT License.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

💡 Future Enhancements

Add support for DOCX input

Improve summarization accuracy with NLP models

Deploy to cloud for public access
