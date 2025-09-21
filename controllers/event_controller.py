from fastapi import APIRouter, HTTPException, status
from models.request import Events , EventType
from models.response import EventResponse
from typing import List
from services.event_service import EventService

router = APIRouter()
service = EventService()

@router.post("/v1/events", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
async def create_event(payload: Events)-> EventResponse:
    events = payload.events
    if not events:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Events list cannot be empty")
   
    for event in events:
        if event.value < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event value number must be a positive number")
    return await service.save_events_to_db(payload)
    
    