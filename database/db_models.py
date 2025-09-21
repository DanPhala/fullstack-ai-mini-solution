from sqlalchemy import (Column,Date,DateTime,Float,Integer,Numeric,String,Text,JSON,)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
import uuid
from datetime import datetime

from .database_connection import Base

class Events(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    timestamp = Column(DateTime(timezone=True), nullable=False, index=True)
    event_type = Column(String, nullable=False) 
    value = Column(Numeric, nullable=False)

class DailyAggregate(Base):
    __tablename__ = "daily_aggregates"

    user_id = Column(UUID(as_uuid=True), primary_key=True)
    date = Column(Date, primary_key=True)
    steps_total = Column(Integer, nullable=False)
    hr_avg = Column(Float, nullable=False)
    sleep_minutes = Column(Integer, nullable=False)
    computed_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)

class ModelRegistry(Base):
    __tablename__ = "model_registry"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version = Column(String, nullable=False)
    path = Column(Text, nullable=False)
    metrics = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)