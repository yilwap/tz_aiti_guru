from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_session
from schemas.orders import OrdersChangeSchema, OrdersResponseSchema
from services.orders import OrdersService

orders_router = APIRouter(prefix="/api/orders", tags=["orders"])


@orders_router.patch("/orders/{orders_id}/")
async def edit_orders(
    orders_id: int,
    params: OrdersChangeSchema,
    session: AsyncSession = Depends(get_session),
) -> OrdersResponseSchema:
    orders_service = OrdersService(session)
    return await orders_service.edit_orders(orders_id, params)
