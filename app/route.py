from fastapi import APIRouter

from app.api.v1 import items


router = APIRouter()

router.include_router(items.router, prefix="/items", tags=["items"])
