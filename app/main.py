# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Créer l'app FastAPI
app = FastAPI(title="Titanic Survival Predictor")

# Charger le modèle
model = joblib.load("model/model.pkl")

# Définir le schéma d'entrée
class Passenger(BaseModel):
    Pclass: int
    Sex: int  # 0 = male, 1 = female
    Age: float
    Fare: float

@app.get("/")
def read_root():
    return {"message": "API Titanic en ligne. Utilisez POST /predict pour faire une prédiction."}

@app.post("/predict")
def predict(passenger: Passenger):
    data = np.array([[passenger.Pclass, passenger.Sex, passenger.Age, passenger.Fare]])
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
