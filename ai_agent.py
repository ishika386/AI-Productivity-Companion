import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def breakdown_task(task):
    prompt = f"""
    You are an expert productivity assistant.

    Break this task into actionable subtasks.

    Task:
    {task}

    Return only bullet points.
    """

    return model.generate_content(prompt).text


def prioritize_tasks(tasks):
    prompt = f"""
    Rank these tasks by urgency and importance.

    Tasks:
    {tasks}

    Return:
    Rank
    Reason
    """

    return model.generate_content(prompt).text


def create_schedule(tasks):
    prompt = f"""
    Create a realistic productivity schedule.

    Tasks:
    {tasks}

    User has 5 free hours.

    Return timetable.
    """

    return model.generate_content(prompt).text


def productivity_coach(message):
    prompt = f"""
    You are a motivational productivity coach.

    User:
    {message}

    Give actionable advice.
    """

    return model.generate_content(prompt).text