from modules.gemini_client import ask_gemini


def get_learning_recommendations(topic: str, level: str = "Beginner") -> str:
    prompt = f"""
Create a personalized learning path for this topic.
Mention beginner, intermediate, and advanced steps.
Also suggest simple resources.

Topic: {topic}
Current level: {level}
"""
    ai_answer = ask_gemini(prompt)
    if ai_answer:
        return ai_answer

    return (
        f"Learning Path for {topic} ({level})\n\n"
        "Beginner:\n"
        "- Learn basic definitions and important terms.\n"
        "- Watch one beginner-friendly video.\n"
        "- Make short notes.\n\n"
        "Intermediate:\n"
        "- Practice small examples or problems.\n"
        "- Read documentation or articles.\n"
        "- Try explaining the concept in your own words.\n\n"
        "Advanced:\n"
        "- Build a small project.\n"
        "- Solve case studies or advanced questions.\n"
        "- Revise and test yourself with quizzes."
    )
