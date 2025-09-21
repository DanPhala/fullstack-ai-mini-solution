from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.database_connection import AsyncDatabase
from database.db_models import Events, DailyAggregate, ModelRegistry 
from controllers import event_controller,aggregate_controller
from controllers import predict_controller

app = FastAPI(title="Backend Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    async with AsyncDatabase.engine.begin() as connection:
        await connection.run_sync(AsyncDatabase.Base.metadata.create_all)

app.include_router(event_controller.router)
app.include_router(aggregate_controller.router)
app.include_router(predict_controller.router)