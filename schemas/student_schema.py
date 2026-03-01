from pydantic import BaseModel, Field
from typing import Optional


# -------------------------
# Request Schema
# -------------------------
class StudentRequest(BaseModel):
    student_id: str = Field(..., example="S101")
    attendance: float = Field(..., ge=0, le=100, example=75)
    internal_marks: float = Field(..., ge=0, le=100, example=60)
    lms_activity_score: float = Field(..., ge=0, le=100, example=50)


# -------------------------
# Response Schemas
# -------------------------
class RiskExplanation(BaseModel):
    attendance_contribution_percent: float
    internal_marks_contribution_percent: float
    lms_activity_contribution_percent: float


class StudentResponse(BaseModel):
    student_id: str
    risk_probability: float
    risk_level: str
    academic_health_score: int
    alert: Optional[str]
    risk_explanation: RiskExplanation