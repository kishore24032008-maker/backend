from pydantic import BaseModel, Field

class StudentData(BaseModel):
    age: int = Field(..., example=20)
    attendance: float = Field(..., example=75.5)
    study_hours: float = Field(..., example=3.5)
    previous_grades: float = Field(..., example=65.0)


class PredictionResponse(BaseModel):
    risk: str