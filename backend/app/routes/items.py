from fastapi import APIRouter
from typing import List
from models.item import Item
from schemas.item import ItemCreate, ItemOut

router = APIRouter()

@router.get("/items", response_model=List[ItemOut])
async def read_items():
    items = await Item.objects.all()
    return items

@router.post("/items", response_model=ItemOut)
async def create_item(item: ItemCreate):
    item_obj = await Item.create(**item.dict())
    return item_obj