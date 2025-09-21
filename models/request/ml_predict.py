from pydantic import BaseModel
from typing import List, Optional

class TrainRow(BaseModel):
    steps_total: int
    hr_avg: Optional[float]
    sleep_minutes: int
    label: int

class TrainPayload(BaseModel):
    rows: List[TrainRow]