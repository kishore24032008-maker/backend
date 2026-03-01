from typing import List
from fastapi import APIRouter
from schemas.student_schema import StudentData, PredictionResponse
from services.prediction_service import predict_student_risk, calculate_risk

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "OK"}


# 🔹 Single Prediction
@router.post("/predict", response_model=PredictionResponse)
def predict(data: StudentData):
    return predict_student_risk(data)


# 🔹 Batch Prediction
@router.post("/predict/batch", response_model=List[PredictionResponse])
def predict_batch(data: List[StudentData]):
    results = []
    for student in data:
        risk = calculate_risk(student)
        results.append({"risk": risk})
    return results