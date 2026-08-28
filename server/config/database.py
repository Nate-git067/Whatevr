#Configuration file configuring the servers database connections 
from server.config.config import POSTGRES_URI
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from typing import AsyncGenerator 


"""Configuring the Postgres database"""
async_engine = create_async_engine(url=POSTGRES_URI)
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=True
)

#Dependency function to create and yield the session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session