from fastapi import FastAPI
from routes.prediction_routes import router as prediction_router

app = FastAPI(
    title="Student Risk Prediction API",
    version="2.0",
    description="AI-powered academic risk detection system"
)

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "running",
        "version": "2.0"
    }

app.include_router(prediction_router)