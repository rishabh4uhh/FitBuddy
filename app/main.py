from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
from app.database import Base, engine

app = FastAPI(title="FitBuddy AI Workout Generator")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)