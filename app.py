from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load the trained model and scaler
model = joblib.load('random_forest_best_model.pkl')  # Replace with your model path
scaler = joblib.load('scaler.pkl')  # Replace with your scaler path

# Define the input schema
class PredictionInput(BaseModel):
    age: int
    education: float
    sex: int
    cigsPerDay: float
    BPMeds: float
    prevalentStroke: int
    prevalentHyp: int
    diabetes: int
    totChol: float
    BMI: float
    heartRate: float
    glucose: float
    MAP: float

# Prediction endpoint
@app.post("/predict")
async def predict(input_data: PredictionInput):
    # Extract input features into a numpy array
    input_features = np.array([[
        input_data.age,
        input_data.education,
        input_data.sex,
        input_data.cigsPerDay,
        input_data.BPMeds,
        input_data.prevalentStroke,
        input_data.prevalentHyp,
        input_data.diabetes,
        input_data.totChol,
        input_data.BMI,
        input_data.heartRate,
        input_data.glucose,
        input_data.MAP
    ]])

    # Scale the input data using the loaded scaler
    scaled_features = scaler.transform(input_features)

    # Perform prediction using the trained model
    prediction = model.predict(scaled_features)

    # Return the prediction as JSON response
    return {"prediction": int(prediction[0])}
