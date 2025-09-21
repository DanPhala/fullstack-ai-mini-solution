from pydantic import BaseModel

class TrainResponse(BaseModel):
    model_path: str
    accuracy: float