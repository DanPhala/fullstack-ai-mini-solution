from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os
from contextlib import asynccontextmanager

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False
)
Base = declarative_base()

class AsyncDatabase:
    engine = engine
    SessionLocal = AsyncSessionLocal
    Base = Base

    @classmethod
    @asynccontextmanager
    async def get_database(cls):
        session = cls.SessionLocal()
        try:
            yield session
        finally:
            await session.close()