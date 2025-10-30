from abc import ABC

from controllers.db.base import BaseControllersInterface, BaseControllers
from models import Categories


class CategoriesControllerInterface(BaseControllersInterface, ABC):
    model: Categories = Categories


class CategoriesController(BaseControllers, CategoriesControllerInterface): ...
