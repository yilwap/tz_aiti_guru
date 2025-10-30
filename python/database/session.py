from typing import AsyncGenerator

from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from settings.db_settings import db_settings

database_url = PostgresDsn.build(
    scheme="postgresql+asyncpg",
    username=db_settings.USER,
    password=db_settings.PASSWORD,
    host=db_settings.HOST,
    port=db_settings.PORT,
    path=db_settings.DATABASE,
)

engine = create_async_engine(database_url.unicode_string(), pool_pre_ping=True)
# noinspection PyTypeChecker
SessionLocal = sessionmaker(  # pylint: disable=C0103
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncGenerator[AsyncSession, ...]:
    async with SessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
