from pathlib import Path
import joblib
from sqlalchemy import text
from helpers.rows_to_array import rows_to_array
from helpers.train_model import train_model
from database.database_connection import AsyncDatabase
from database.db_models import ModelRegistry
from datetime import datetime
from models.response.trained_model import TrainResponse
from models.response.energy_prediction import PredictResponse
from models.request.energy_prediction import PredictPayload

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

    async def predict(self, payload: PredictPayload) -> PredictResponse:
        async with AsyncDatabase.get_database() as session:
            latest_model = await session.execute(
                text("SELECT * FROM model_registry ORDER BY created_at DESC LIMIT 1")
            )
            model_row = latest_model.fetchone()
            if not model_row:
                raise ValueError("No trained model found.")
            model_path = model_row.path
            version = model_row.version

        model = joblib.load(model_path)

        if payload.features:
            features = [payload.features.steps_total, payload.features.hr_avg, payload.features.sleep_minutes]
        elif payload.user_id and payload.date:
            async with AsyncDatabase.get_database() as session:
                result = await session.execute(
                    "SELECT steps_total, hr_avg, sleep_minutes FROM daily_aggregate WHERE user_id=:user_id AND date=:date",
                    {"user_id": str(payload.user_id), "date": str(payload.date)}
                )
                row = result.fetchone()
                if not row:
                    raise Exception("No aggregate data found for user/date.")
                features = [row.steps_total, row.hr_avg, row.sleep_minutes]
        else:
            raise Exception("Invalid payload.")
        
        probability = float(model.predict_proba([features])[0][1])
        prediction = bool(model.predict([features])[0])

        return PredictResponse(
            version=version,
            probability=probability,
            prediction=prediction
        )

