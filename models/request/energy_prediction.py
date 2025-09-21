from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class FeaturesPayload(BaseModel):
    steps_total: int
    hr_avg: float
    sleep_minutes: int

class PredictPayload(BaseModel):
    user_id: Optional[UUID] = None
    date: Optional[date] = None
    features: Optional[FeaturesPayload] = None