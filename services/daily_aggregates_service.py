from database.database_connection import AsyncDatabase
from database.db_models import Events
from models.response.daily_aggregate import AggregateResponse
from uuid import UUID
from sqlalchemy import select, func

class DailyAggregatesService:
    def __init__(self):
        pass

    async def compute_aggregate_service(self, user_id: UUID, date):
        date_str = date.strftime('%Y-%m-%d')
        async with AsyncDatabase.get_database() as session:
            date_filter = func.to_char(Events.timestamp, 'YYYY-MM-DD') == date_str
            steps_total_query = select(func.sum(Events.value)).where(
                Events.user_id == user_id,
                Events.event_type == "steps",
                date_filter             
            )
            steps_total_result = await session.execute(steps_total_query)
            steps_total = steps_total_result.scalar() or 0

            hr_avg_query = select(func.avg(Events.value)).where(
                Events.user_id == user_id,
                Events.event_type == "heart_rate",
                date_filter
            )

            hr_avg_result = await session.execute(hr_avg_query)
            hr_avg = hr_avg_result.scalar()
            hr_avg = float(hr_avg) if hr_avg is not None else None

            sleep_total_query = select(func.sum(Events.value)).where(
                Events.user_id == user_id,
                Events.event_type == "sleep",
                date_filter
            )
            sleep_total_result = await session.execute(sleep_total_query)
            sleep_minutes = sleep_total_result.scalar() or 0

            return AggregateResponse(
                user_id=user_id,
                date=date,
                steps_total=int(steps_total),
                hr_avg=hr_avg,
                sleep_minutes=int(sleep_minutes),
                computed_at=str(date)
            )