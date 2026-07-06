from modules.gemini_client import ask_gemini


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, a friendly study assistant.
Answer the student's question in simple language.
Keep the answer clear and useful.

Question: {question}
"""
    ai_answer = ask_gemini(prompt)
    if ai_answer:
        return ai_answer

    return (
        "I could not connect to Gemini because the API key is not added yet.\n\n"
        f"Here is a simple study-style response for your question: {question}\n"
        "Try breaking the topic into definition, main points, example, and revision notes."
    )
