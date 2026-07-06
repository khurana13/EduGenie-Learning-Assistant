# EduGenie Learning Assistant

EduGenie Learning Assistant is a simple AI-powered educational web application that helps students with question answering, concept explanation, quiz generation, text summarization, and learning path recommendations.

The project is built using FastAPI for the backend and HTML, CSS, and JavaScript for the frontend. It uses the Gemini API to generate educational responses.

---

## Features

- Ask academic questions
- Get simple explanations of difficult topics
- Generate quiz questions from a topic or passage
- Summarize long text
- Get a basic learning path for any topic
- Simple and clean user interface
- FastAPI-based backend
- Local deployment using Uvicorn

---

## Tech Stack

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- Jinja2
- Uvicorn
- Gemini API

---

## Project Structure

```bash
EduGenie-Learning-Assistant/
│
├── main.py
├── requirements.txt
├── .env.example
├── README.md
│
├── modules/
│   ├── qna.py
│   ├── explanation_module.py
│   ├── quiz_module.py
│   ├── summary_module.py
│   └── learning_path.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
