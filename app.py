from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Customer Churn Prediction API")

class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    # Dummy logic (model can be plugged later)
    churn_probability = 0.5
    churn_prediction = 1 if churn_probability >= 0.35 else 0

    return {
        "churn_probability": churn_probability,
        "churn_prediction": churn_prediction
    }
