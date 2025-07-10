# 🤖 Resume AI Chatbot

This is a **ChatGPT-like AI Assistant** that reads your resume and answers questions from it intelligently. It uses RAG (Retrieval-Augmented Generation) with **Hugging Face transformers**, **sentence-transformers**, and **Streamlit** — no OpenAI API required!

---

## 🔥 Features

- ✅ Ask questions about your own resume (PDF format)
- ✅ Uses RAG (semantic search + QA)
- ✅ Powered by Hugging Face (`deepset/roberta-base-squad2`)
- ✅ ChatGPT-style interface with chat history
- ✅ Rule-based fallback for questions like email, phone, skills
- ✅ Fully private and Open Source — no external API calls
- ✅ Deployable with 1-click on Streamlit Cloud

---

## 📸 Demo Screenshot

![screenshot](./assets/demo.png) <!-- Add your own screenshot here -->

---

## 🧠 How It Works

1. You upload your resume (`.pdf`)
2. It extracts the text using `pdfplumber`
3. Chunks are created and embedded using `all-MiniLM-L6-v2`
4. Your question is semantically matched with the most relevant chunks
5. The selected context is passed to a Hugging Face QA model
6. The answer is generated and shown ChatGPT-style

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Streamlit` | UI Framework |
| `sentence-transformers` | For semantic search |
| `transformers` | Hugging Face QA model |
| `pdfplumber` | Extracts text from resume PDFs |
| `torch` | Backend for model inference |

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/nirala7765/resume_reader.git
cd resume-ai-chatbot


2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
streamlit run app.py
🌐 Deploy on Streamlit Cloud
✅ 1. Push to GitHub
Make sure you push the entire project folder (including requirements.txt, app.py, and rag_utils.py) to a GitHub repository.

🚀 2. Deploy
Go to: https://streamlit.io/cloud

Click "Deploy an app"

Select your repo and branch

Set app.py as the main file

Click Deploy

📁 Project Structure
bash
Copy
Edit
resume-ai-chatbot/
│
├── app.py               # Main Streamlit application
├── rag_utils.py         # Helper functions for text processing and rule-based QA
├── requirements.txt     # Python dependencies
├── assets/demo.png      # Demo screenshot (optional)
└── sample_resume.pdf    # Sample resume (optional)
✨ Sample Questions You Can Ask
What are my cloud skills?

Where did I last work?

What programming languages do I know?

What are my certifications?

What's my mobile number or email?

Tell me about my projects.

What frameworks have I used?

🤖 Model Used
Embedding model: sentence-transformers/all-MiniLM-L6-v2

QA model: deepset/roberta-base-squad2

Both models run locally via Hugging Face — no API key or internet required after install.

🛡️ Privacy
This tool runs entirely on your local machine or server. Your resume is not sent to any external service — keeping your personal data private and secure.

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Arun Kumar
Built with ❤️ to help candidates practice confidently.

⭐️ Show Your Support
If you find this useful:

🌟 Star the repo

🍴 Fork it

🐛 Open issues for bugs or feature suggestions

📬 Contact
For queries, improvements, or collaborations:
📧 kravikant249@gmail.com
📱 +91-7765011865


