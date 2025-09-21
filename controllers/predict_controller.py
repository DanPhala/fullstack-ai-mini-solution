from fastapi import APIRouter, HTTPException, status
from models.request.ml_predict import TrainPayload
from services.ml_service.ml_service import MLService
from models.response.trained_model import TrainResponse

router = APIRouter()
ml_service = MLService()

@router.post("/v1/ml/train")
async def train_model(payload: TrainPayload) -> TrainResponse:
    if not payload.rows or len(payload.rows) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data provided for training.")
    try:
        model_info = await ml_service.train_and_persist_model(payload.rows)
        return model_info
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))