# backend/app/routes/__init__.py

from fastapi import APIRouter
from .items import router as items_router

router = APIRouter()

router.include_router(items_router, prefix="/items", tags=["items"])