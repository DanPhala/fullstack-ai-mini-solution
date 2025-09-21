from pydantic import BaseModel
from uuid import UUID

class EventResponse(BaseModel):
    user_id: UUID
    count: int
