from abc import ABC, abstractmethod

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from controllers.db.nomenclature import NomenclatureController
from controllers.db.orders import OrdersController, OrdersControllerInterface
from controllers.db.orders_to_nomenclature import Orders2NomenclatureController
from models import Nomenclature, Orders, Orders2Nomenclature
from schemas.clients import ClientsSchemas
from schemas.orders import (
    OrdersChangeSchema,
    OrdersResponseSchema,
    OrderNomenclatureSchemas,
)


class OrdersServiceInterface(ABC):
    orders_controller: OrdersControllerInterface

    @abstractmethod
    def __init__(self, session: AsyncSession): ...

    @abstractmethod
    async def edit_orders(
        self, orders_id: int, params: OrdersChangeSchema
    ) -> OrdersResponseSchema: ...


class OrdersService(OrdersServiceInterface):
    def __init__(self, session: AsyncSession):
        self.orders_controller = OrdersController(session)
        self.nomenclature_controller = NomenclatureController(session)
        self.orders_to_nomenclature_controller = Orders2NomenclatureController(session)

    async def edit_orders(
        self, orders_id: int, params: OrdersChangeSchema
    ) -> OrdersResponseSchema:
        orders: Orders = await self.orders_controller.get_by_id(orders_id)
        if orders is None:
            raise HTTPException(status_code=404, detail="Order not found")

        nomenclature: Nomenclature = await self.nomenclature_controller.get_by_id(
            params.nomenclature_id
        )
        if nomenclature is None:
            raise HTTPException(status_code=404, detail="Nomenclature not found")

        if nomenclature.count < params.count:
            raise HTTPException(status_code=400, detail="count is too big")

        orders_to_nomenclature: Orders2Nomenclature = (
            await self.orders_to_nomenclature_controller.get_by_order_and_nomenclature_ids(
                order_id=orders_id,
                nomenclature_id=nomenclature.id,
            )
        )
        if orders_to_nomenclature is not None:
            orders_to_nomenclature.count += params.count
            nomenclature.count -= params.count
            await self.orders_to_nomenclature_controller.update(orders_to_nomenclature)
            await self.nomenclature_controller.update(nomenclature)
            orders = await self.orders_controller.reload(orders_id)
            return self._get_response(orders)

        await self.orders_to_nomenclature_controller.create(
            nomenclature_id=nomenclature.id,
            orders_id=orders_id,
            count=params.count,
        )
        nomenclature.count -= params.count
        await self.nomenclature_controller.update(nomenclature)
        orders = await self.orders_controller.reload(orders_id)
        return self._get_response(orders)

    @staticmethod
    def _get_response(orders: Orders) -> OrdersResponseSchema:
        # noinspection PyArgumentList
        nomenclature_res = [
            OrderNomenclatureSchemas(
                count=orders2nomenclature.count,
                nomenclature_id=orders2nomenclature.nomenclature_id,
                nomenclature_name=orders2nomenclature.nomenclature.name,
            )
            for orders2nomenclature in orders.orders2nomenclature
        ]

        return OrdersResponseSchema(
            id=orders.id,
            clients=ClientsSchemas(
                id=orders.clients.id,
                name=orders.clients.name,
                address=orders.clients.address,
            ),
            nomenclature=nomenclature_res,
            timestamp=orders.created_date,
        )
