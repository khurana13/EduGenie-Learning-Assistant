from modules.gemini_client import ask_gemini


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational content in simple words.
Keep only the important points.

Text:
{text}
"""
    ai_answer = ask_gemini(prompt)
    if ai_answer:
        return ai_answer

    sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
    short_summary = ". ".join(sentences[:3])
    return short_summary + "." if short_summary else "Summary could not be generated."
