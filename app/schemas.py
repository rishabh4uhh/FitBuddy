from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    age: int
    weight: int
    goal: str
    intensity: str

class FeedbackRequest(BaseModel):
    user_id: int
    feedback: str