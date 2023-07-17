from fastapi import APIRouter

router = APIRouter()

"""定义路由和请求处理函数"""


@router.get("/items")
async def get_items():
    # 处理获取 items 的逻辑
    return {"message": "Get items 666"}


@router.post("/items")
async def create_item():
    # 处理创建 item 的逻辑
    return {"message": "Create item"}
