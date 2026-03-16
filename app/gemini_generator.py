import google.generativeai as genai
import os
from dotenv import load_dotenv
import time
from google.api_core.exceptions import ResourceExhausted
from typing import Optional

load_dotenv()  # loads .env file

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model_pro = genai.GenerativeModel("gemini-2.5-flash")
model_flash = genai.GenerativeModel("gemini-2.5-flash")


def generate_workout_gemini(goal: str, intensity: str) -> str:
    """
    Generate a 5-day workout plan using Gemini AI based on goal and intensity.
    Falls back to a sample plan if API quota is exceeded.
    """

    prompt = f"""
You are a professional fitness trainer.

Create a structured 5-day workout plan.

Goal: {goal}
Intensity: {intensity}

Include:
- Day wise workout
- Exercise name
- Sets and reps
- Rest time

Also include one nutrition tip.
"""

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model_pro.generate_content(prompt)
            return response.text
        except ResourceExhausted as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # exponential backoff
                time.sleep(wait_time)
            else:
                # Fallback to static plan
                return f"""
Sample 5-Day Workout Plan for {goal} with {intensity} intensity:

Day 1: Push - Bench Press 3x10, Overhead Press 3x10, Tricep Dips 3x12, Rest 60s
Day 2: Pull - Deadlifts 3x8, Pull-ups 3x8, Bicep Curls 3x12, Rest 60s
Day 3: Legs - Squats 3x10, Lunges 3x10 per leg, Calf Raises 3x15, Rest 60s
Day 4: Rest or Light Cardio
Day 5: Full Body - Rows 3x10, Push-ups 3x10, Planks 3x30s, Rest 60s

Nutrition Tip: Eat a balanced diet with plenty of protein and vegetables.
"""
    return "Unexpected error"


def generate_nutrition_tip(goal: str) -> str:
    """
    Generate a short nutrition tip using Gemini AI based on goal.
    Falls back to a generic tip if API quota is exceeded.
    """

    prompt = f"Give a short nutrition tip for someone whose goal is {goal}"

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model_flash.generate_content(prompt)
            return response.text
        except ResourceExhausted as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
            else:
                # Fallback tip
                return f"For {goal}, focus on eating whole foods and staying hydrated."
    return "Unexpected error"


def update_workout_plan(original_plan: str, feedback: str) -> str:
    """
    Update the workout plan using Gemini AI based on user feedback.
    Falls back to the original plan with a note if API quota is exceeded.
    """

    prompt = f"""
    Update the following workout plan based on feedback.

    Workout Plan:
    {original_plan}

    Feedback:
    {feedback}
    """

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model_pro.generate_content(prompt)
            return response.text
        except ResourceExhausted as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
            else:
                # Fallback: return original with note
                return f"{original_plan}\n\nUpdated based on feedback: {feedback} (Note: AI update failed due to quota, please adjust manually)."
    return "Unexpected error"