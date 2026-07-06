import json
import re
from modules.gemini_client import ask_gemini


def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```json", "", text)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)
    return text.strip()


def fallback_quiz(topic: str):
    return [
        {
            "question": f"What is the main idea of {topic}?",
            "options": ["Basic concept", "Unrelated topic", "Random number", "None of these"],
            "correct_answer": "Basic concept",
        },
        {
            "question": f"Why should students learn {topic}?",
            "options": ["For better understanding", "To avoid studying", "Only for marks", "No reason"],
            "correct_answer": "For better understanding",
        },
        {
            "question": f"Which method is best for learning {topic}?",
            "options": ["Step-by-step practice", "Guessing", "Skipping basics", "Memorizing only"],
            "correct_answer": "Step-by-step practice",
        },
    ]


def generate_quiz(text: str):
    prompt = f"""
Create exactly 3 MCQ questions from the given topic or passage.
Return only valid JSON as a list.
Each object must have: question, options, correct_answer.
Options should be a list of 4 strings.

Topic or passage:
{text}
"""
    ai_answer = ask_gemini(prompt)
    if not ai_answer:
        return fallback_quiz(text[:60])

    try:
        cleaned = clean_json_block(ai_answer)
        return json.loads(cleaned)
    except Exception:
        return {
            "note": "AI response was generated but could not be parsed as JSON.",
            "raw_response": ai_answer,
        }
