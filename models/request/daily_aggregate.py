from pydantic import BaseModel
from uuid import UUID
from datetime import date

class AggregateRequest(BaseModel):
    date: date