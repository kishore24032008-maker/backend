from fastapi import FastAPI
from api.v1.routes import prediction_routes

app = FastAPI(
    title="Student Risk Prediction API",
    version="1.0.0"
)

app.include_router(
    prediction_routes.router,
    prefix="/api/v1",
    tags=["Prediction"]
)