from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.gemini_generator import generate_workout_gemini, generate_nutrition_tip, update_workout_plan

router = APIRouter()

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/generate-workout")
def generate_workout(
        request: Request,
        name: str = Form(...),
        age: int = Form(...),
        weight: int = Form(...),
        goal: str = Form(...),
        intensity: str = Form(...),
        db: Session = Depends(get_db)
):

    workout_plan = generate_workout_gemini(goal, intensity)
    nutrition_tip = generate_nutrition_tip(goal)

    user = User(
        name=name,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity,
        original_plan=workout_plan
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "username": name,
        "goal": goal,
        "intensity": intensity,
        "workout_plan": workout_plan,
        "nutrition_tip": nutrition_tip,
        "user_id": user.id
    })


@router.post("/submit-feedback")
def submit_feedback(
        request: Request,
        user_id: int = Form(...),
        feedback: str = Form(...),
        db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    updated_plan = update_workout_plan(user.original_plan, feedback)

    user.updated_plan = updated_plan
    db.commit()

    return templates.TemplateResponse("result.html", {
        "request": request,
        "username": user.name,
        "goal": user.goal,
        "intensity": user.intensity,
        "workout_plan": updated_plan,
        "nutrition_tip": "",
        "user_id": user.id
    })


@router.get("/view-all-users")
def view_all_users(request: Request, db: Session = Depends(get_db)):

    users = db.query(User).all()

    return templates.TemplateResponse(
        "all_users.html",
        {"request": request, "users": users}
    )