from abc import ABC

from controllers.db.base import BaseControllersInterface, BaseControllers
from models import Orders


class OrdersControllerInterface(BaseControllersInterface, ABC):
    model: Orders = Orders


class OrdersController(BaseControllers, OrdersControllerInterface): ...
