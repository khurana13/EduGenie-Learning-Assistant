import os
from dotenv import load_dotenv

load_dotenv()


def ask_gemini(prompt: str):
    """Small helper for Gemini. Returns None when API key is missing.

    The project still works without an API key by using simple fallback logic.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

    if not api_key:
        return None

    try:
        import google.generativeai as genai

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as error:
        return f"Gemini error: {error}"
