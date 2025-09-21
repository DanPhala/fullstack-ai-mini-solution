from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
import asyncio
import json

router = APIRouter()
user_event_queues = {}

async def event_generator(user_id: str):
    queue = user_event_queues.setdefault(user_id, asyncio.Queue())
    while True:
        data = await queue.get()
        sse_data = f"data: {json.dumps(data)}\n\n"
        yield sse_data

@router.get("/v1/stream/{user_id}")
async def stream_user_aggregates(user_id: str, request: Request):
    async def streamer():
        async for event in event_generator(user_id):
            if await request.is_disconnected():
                break
            yield event
    return StreamingResponse(streamer(), media_type="text/event-stream")
