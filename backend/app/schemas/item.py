from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str
    price: float


class ItemCreate(ItemBase):
    pass


class ItemOut(ItemBase):
    id: int

    class Config:
        orm_mode = True