from pydantic import BaseModel,ConfigDict
from uuid import UUID

class AggregateResponse(BaseModel):
    user_id: UUID
    steps_total: int
    hr_avg: float | None
    sleep_minutes: int
    computed_at: str

    model_config = ConfigDict(from_attributes=True)