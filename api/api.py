from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from load_data.load_data import load_model

app = FastAPI(title="Credit Card Fraud Detection API")

# Load the trained model once at startup
model_path = load_model()
model = joblib.load(model_path)


class TransactionData(BaseModel):
    features: list[float]  # Pass the transaction feature values as a list


class PredictionResponse(BaseModel):
    prediction: int          # 0 = Legitimate, 1 = Fraud
    label: str
    confidence: float        # Probability of fraud


@app.get("/")
def root():
    return {"message": "Credit Card Fraud Detection API is running"}


@app.post("/predict", response_model=PredictionResponse)
def predict(data: TransactionData):
    try:
        input_array = np.array(data.features).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0][1]  # Fraud probability

        return PredictionResponse(
            prediction=int(prediction),
            label="Fraud" if prediction == 1 else "Legitimate",
            confidence=round(float(probability), 4)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}