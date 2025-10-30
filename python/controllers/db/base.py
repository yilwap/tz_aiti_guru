from abc import ABC, abstractmethod
from typing import Optional, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.base import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseControllersInterface(ABC):
    model: ModelType
    _session: AsyncSession

    @abstractmethod
    def __init__(self, session: AsyncSession) -> None: ...

    @abstractmethod
    async def get_by_id(self, id_: int) -> Optional[ModelType]: ...

    @abstractmethod
    async def update(self, obj: Base) -> ModelType: ...

    @abstractmethod
    async def create(self, *args, **kwargs) -> ModelType: ...

    @abstractmethod
    async def reload(self, id_: int) -> Optional[ModelType]: ...


class BaseControllers(BaseControllersInterface):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, id_: int) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == id_)
        return (await self._session.execute(query)).scalar_one_or_none()

    async def update(self, obj: Base) -> ModelType:
        self._session.add(obj)
        await self._session.commit()
        await self._session.refresh(obj)
        return obj

    async def create(self, *args, **kwargs) -> ModelType:
        model = self.model(**kwargs)
        self._session.add(model)
        await self._session.commit()
        return model

    async def reload(self, id_: int) -> Optional[ModelType]:
        model = await self.get_by_id(id_)
        await self._session.refresh(model)
        return model
