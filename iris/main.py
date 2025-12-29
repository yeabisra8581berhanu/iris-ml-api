from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Enable CORS so your Vercel frontend can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.get("/predict")
async def predict_page():
    return FileResponse("static/predict.html")

# Load artifacts (Ensure these files are in the same folder)
lr_model = joblib.load('models/logistic_model.pkl')
dt_model = joblib.load('models/decision_tree_model.pkl')
scaler = joblib.load('models/scaler.pkl')

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    model_choice: str  # "logistic" or "decision_tree"

@app.post("/predict")
async def predict(data: IrisInput):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    scaled_features = scaler.transform(features)
    
    model = lr_model if data.model_choice == "logistic" else dt_model
    prediction = model.predict(scaled_features)
    
    target_names = ['Setosa', 'Versicolor', 'Virginica']
    return {"prediction": target_names[int(prediction[0])]}