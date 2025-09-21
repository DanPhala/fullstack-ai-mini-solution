from pathlib import Path
import joblib
from helpers.rows_to_array import rows_to_array
from helpers.train_model import train_model
from database.database_connection import AsyncDatabase
from database.db_models import ModelRegistry
from datetime import datetime
from models.response.trained_model import TrainResponse

class MLService:
    async def train_and_persist_model(self, rows) -> TrainResponse:
        x, y = rows_to_array(rows)
        model, acc = train_model(x, y)
        Path("ML/models").mkdir(parents=True, exist_ok=True)
        model_path = "ML/models/model.pkl"
        joblib.dump(model, model_path)
        async with AsyncDatabase.get_database() as session:
            registry = ModelRegistry(
                version="v1",  
                path=model_path,
                metrics={"accuracy": acc},
                created_at=datetime.utcnow()
            )
            session.add(registry)
            await session.commit()
        return TrainResponse(model_path=model_path, accuracy=acc)