from fastapi import APIRouter
from schemas.student_schema import StudentData, PredictionResponse
from services.prediction_service import predict_student_risk

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "OK"}


@router.post("/predict", response_model=PredictionResponse)
def predict(data: StudentData):
    result = predict_student_risk(data)
    return result