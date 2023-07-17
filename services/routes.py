from fastapi import APIRouter
from ..db.connection import SessionLocal
from ..db.models import Item

router = APIRouter()


@router.get("/items")
async def get_items():
    db = SessionLocal()
    items = db.query(Item).all()
    return {"items": items}


@router.post("/items")
async def create_item(item: Item):
    db = SessionLocal()
    db.add(item)
    db.commit()
    db.refresh(item)
    return {"item": item}
