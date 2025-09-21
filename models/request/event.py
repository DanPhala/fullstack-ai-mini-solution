from pydantic import BaseModel
from typing import Literal
from uuid import UUID
from datetime import datetime
from typing import List
from enum import Enum

class EventType(str, Enum):
    heart_rate = "heart_rate"
    steps = "steps"
    sleep = "sleep"
class Event(BaseModel):
    user_id: UUID
    timestamp: datetime
    event_type: EventType
    value: float
class Events(BaseModel):
    events: List[Event]

