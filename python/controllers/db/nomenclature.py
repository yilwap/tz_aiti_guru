from abc import ABC

from controllers.db.base import BaseControllersInterface, BaseControllers
from models import Nomenclature


class NomenclatureControllerInterface(BaseControllersInterface, ABC):
    model: Nomenclature = Nomenclature


class NomenclatureController(BaseControllers, NomenclatureControllerInterface): ...
