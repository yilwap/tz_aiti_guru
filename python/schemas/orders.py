from datetime import datetime

from pydantic import BaseModel, PositiveInt, Field

from schemas.clients import ClientsSchemas


class OrdersChangeSchema(BaseModel):
    nomenclature_id: int = Field(alias="nomenclatureId", default=None)
    count: PositiveInt

    class Config:
        validate_by_name = True
        validate_by_alias = True
        populate_by_name = True


class OrderNomenclatureSchemas(BaseModel):
    nomenclature_id: int = Field(alias="nomenclatureId", default=None)
    nomenclature_name: str = Field(alias="nomenclatureName", default=None)
    count: PositiveInt

    class Config:
        validate_by_name = True
        validate_by_alias = True
        populate_by_name = True


class OrdersResponseSchema(BaseModel):
    id_: int = Field(alias="id", default=None)
    nomenclature: list[OrderNomenclatureSchemas]
    clients: ClientsSchemas
    timestamp: datetime

    class Config:
        validate_by_name = True
        validate_by_alias = True
        populate_by_name = True
