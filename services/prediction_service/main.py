from fastapi import FastAPI
from detect_fake import FakeNewsDetector
from shared_models.prediction_models import PredictionInput, PredictResponse
import os

app = FastAPI()

MODEL_FILE = 'fake_news_model.pkl'
CSV_FILE = 'news.csv'

# Initialize the model
if not os.path.exists(MODEL_FILE):
    print("Model not found. Training new model...")
    detector = FakeNewsDetector()
    detector.train(CSV_FILE)
    detector.save_model(MODEL_FILE)
    print("Model trained and saved.")
else:
    print("Loading existing model...")

detector = FakeNewsDetector.load_model(MODEL_FILE)

@app.post("/predict", response_model=PredictResponse)
async def predict(input_data: PredictionInput):
    return detector.predict(input_data.text)

@app.get("/health")
async def health():
    return {"message": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
