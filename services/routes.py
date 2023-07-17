from fastapi import APIRouter
from db.models import Item

router = APIRouter()


@router.get("/get_items")
async def get_items():
    items = await Item.all()
    return {"items": items}


@router.post("/create_item")
async def create_item(item: Item):
    await Item(item).save()
    return {"item": item}
