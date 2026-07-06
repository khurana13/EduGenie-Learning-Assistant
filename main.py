from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from modules.qna import answer_question
from modules.explanation_module import explain_topic
from modules.quiz_module import generate_quiz
from modules.summary_module import summarize_text
from modules.learning_path import get_learning_recommendations
from modules.data_store import save_activity

app = FastAPI(title="EduGenie Learning Assistant")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextInput(BaseModel):
    text: str


class QuestionInput(BaseModel):
    question: str


class TopicInput(BaseModel):
    topic: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)


@app.post("/qa")
def qa_api(data: QuestionInput):
    if not data.question.strip():
        return JSONResponse(status_code=400, content={"error": "Please enter a question."})

    answer = answer_question(data.question)
    save_activity("QnA", data.question, answer)
    return {"question": data.question, "answer": answer}


@app.post("/explain")
def explain_api(data: TopicInput):
    if not data.topic.strip():
        return JSONResponse(status_code=400, content={"error": "Please enter a topic."})

    explanation = explain_topic(data.topic)
    save_activity("Explanation", data.topic, explanation)
    return {"topic": data.topic, "explanation": explanation}


@app.post("/quiz")
def quiz_api(data: TextInput):
    if not data.text.strip():
        return JSONResponse(status_code=400, content={"error": "Please enter a topic or passage."})

    quiz = generate_quiz(data.text)
    save_activity("Quiz", data.text, quiz)
    return {"quiz": quiz}


@app.post("/summarize")
def summarize_api(data: TextInput):
    if not data.text.strip():
        return JSONResponse(status_code=400, content={"error": "Please enter text to summarize."})

    summary = summarize_text(data.text)
    save_activity("Summary", data.text, summary)
    return {"summary": summary}


@app.get("/learn/recommendations")
def learning_api(topic: str = Query(...), level: str = Query("Beginner")):
    if not topic.strip():
        return JSONResponse(status_code=400, content={"error": "Please enter a topic."})

    plan = get_learning_recommendations(topic, level)
    save_activity("Learning Path", f"{topic} - {level}", plan)
    return {"topic": topic, "level": level, "learning_path": plan}
