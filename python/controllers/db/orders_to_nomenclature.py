from abc import ABC

from sqlalchemy import select

from controllers.db.base import BaseControllersInterface, BaseControllers
from models import Orders2Nomenclature


class Orders2NomenclatureControllerInterface(BaseControllersInterface, ABC):
    model: Orders2Nomenclature = Orders2Nomenclature


class Orders2NomenclatureController(
    BaseControllers, Orders2NomenclatureControllerInterface
):

    async def get_by_order_and_nomenclature_ids(self, order_id, nomenclature_id):
        query = (
            select(self.model)
            .where(self.model.orders_id == order_id)
            .where(self.model.nomenclature_id == nomenclature_id)
        )
        return (await self._session.execute(query)).scalar_one_or_none()
