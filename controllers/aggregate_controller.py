from fastapi import APIRouter, HTTPException, status, Depends
from models.request import Events , EventType
from models.response import EventResponse
from typing import List
from services.event_service import EventService
from models.request.daily_aggregate import AggregateRequest
from models.response.daily_aggregate import AggregateResponse
from services.daily_aggregates_service import DailyAggregatesService
# from models.response.daily_aggregate import DailyAggregateResponse
from datetime import date
from uuid import UUID

router = APIRouter()
service = DailyAggregatesService()

@router.post("/v1/aggregate/{user_id}", response_model=AggregateResponse, status_code=status.HTTP_201_CREATED)
async def compute_daily_aggregate(user_id: UUID, payload: AggregateRequest) -> AggregateResponse:
    date = payload.date
    if not date:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Date cannot be empty")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID cannot be empty")
    try:
        result = await service.compute_aggregate_service(user_id, payload.date)
        return result
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))

@router.get("/v1/users/{user_id}/daily/{date}")
async def get_daily_aggregate(user_id: UUID, date: date):
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID cannot be empty")
    if not date:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Date cannot be empty")
    result = await service.get_daily_aggregate(user_id, date)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Daily aggregate not found")
    # return DailyAggregateResponse.model_validate(result) 
    return result