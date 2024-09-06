from pydantic import BaseModel

class PredictResponse(BaseModel):
    real: bool
    confidence: float

class PredictionInput(BaseModel):
    text: str
