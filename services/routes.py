from fastapi import APIRouter
from db.models import Item, ItemPydantic

router = APIRouter()


@router.get("/get_items")
async def get_items():
    # items = await Item.all()
    # return {"items": items}
    items = await ItemPydantic.from_queryset(Item.all())
    return {"items": items}


@router.post("/create_item", response_model=ItemPydantic)
async def create_item(item: ItemPydantic):
    # **item  的作用是将 Pydantic 模型实例转换为字典，并将字典中的键值对作为关键字参数传递给函数。这样可以方便地将模型的字段值传递给需要接收关键字参数的函数
    # await Item.create(**item.dict(exclude_unset=True))
    # 。 exclude_unset=True  参数的作用是排除那些未设置值的字段，只包含已设置的字段
    item_obj = await Item.create(**item.model_dict(exclude_unset=True))
    # item_obj = await Item.create(**item.dict())
    return item_obj
