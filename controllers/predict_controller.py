from fastapi import APIRouter, HTTPException, status
from models.request.ml_predict import TrainPayload
from services.ml_service.ml_service import MLService
from models.response.trained_model import TrainResponse
from models.response.energy_prediction import PredictResponse
from models.request.energy_prediction import PredictPayload

router = APIRouter()
ml_service = MLService()

@router.post("/v1/train")
async def train_model(payload: TrainPayload) -> TrainResponse:
    if not payload.rows or len(payload.rows) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data provided for training.")
    try:
        model_info = await ml_service.train_and_persist_model(payload.rows)
        return model_info
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/v1/predict", response_model=PredictResponse)
async def predict(payload: PredictPayload) -> PredictResponse:
    if not ((payload.features) or (payload.user_id and payload.date)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Either features or user_id and date must be provided.")
    try:
        prediction = await ml_service.predict(payload)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))