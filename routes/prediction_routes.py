from fastapi import APIRouter, Depends
from typing import List
from schemas.student_schema import StudentRequest, StudentResponse
from services.prediction_service import PredictionService

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


def get_prediction_service():
    return PredictionService()


@router.post(
    "/single",
    response_model=StudentResponse
)
def predict(
    student: StudentRequest,
    service: PredictionService = Depends(get_prediction_service)
):
    return service.calculate_prediction(student)


@router.post(
    "/batch",
    response_model=List[StudentResponse]
)
def batch_predict(
    students: List[StudentRequest],
    service: PredictionService = Depends(get_prediction_service)
):
    return [service.calculate_prediction(student) for student in students]