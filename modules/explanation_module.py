from modules.gemini_client import ask_gemini


def explain_topic(topic: str) -> str:
    prompt = f"""
Explain this topic like a teacher explaining to a beginner.
Use short points and one small example.

Topic: {topic}
"""
    ai_answer = ask_gemini(prompt)
    if ai_answer:
        return ai_answer

    return (
        f"{topic} is an important concept that can be understood step by step.\n\n"
        "1. First, learn the basic meaning of the topic.\n"
        "2. Then understand where it is used.\n"
        "3. Finally, practice with small examples.\n\n"
        f"Example: If you are learning {topic}, write its definition, one use case, and one real-life example."
    )
