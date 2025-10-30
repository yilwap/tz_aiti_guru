from pydantic import BaseModel, Field


class ClientsSchemas(BaseModel):
    id_: int = Field(alias="id")
    name: str
    address: str
