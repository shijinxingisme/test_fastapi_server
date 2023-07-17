class SomeService:
    def get_item(self, item_id: int):
        # 处理获取 item 的逻辑
        return {"id": item_id, "name": "Item", "price": 10.0}

    def create_item(self, item_data: dict):
        # 处理创建 item 的逻辑
        return {"message": "Item created"}
