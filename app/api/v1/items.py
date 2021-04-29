from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_items():
    return [{"item_id": 1}]


@router.get("/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
