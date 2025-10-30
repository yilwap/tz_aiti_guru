from abc import ABC

from controllers.db.base import BaseControllersInterface, BaseControllers
from models import Clients


class ClientsControllerInterface(BaseControllersInterface, ABC):
    model: Clients = Clients


class ClientsController(BaseControllers, ClientsControllerInterface): ...
