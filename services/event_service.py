from models.request import Events
from models.response import EventResponse
from database.database_connection import AsyncDatabase
from database.db_models import Events as EventsModel

class EventService:
    def __init__(self):
        pass
    async def save_events_to_db(self, events: Events) -> EventResponse:
        async with AsyncDatabase.get_database() as session:
            for event in events.events:
                db_event = EventsModel(
                    user_id=event.user_id,
                    timestamp=event.timestamp,
                    event_type=event.event_type.value,
                    value=event.value
                )
                session.add(db_event)
            await session.commit()
            user_id = events.events[0].user_id if events.events else None
            count = len(events.events)
            return EventResponse(user_id=user_id, count=count)