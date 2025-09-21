from pydantic import BaseModel

class PredictResponse(BaseModel):
    version: str
    probability: float
    prediction: bool