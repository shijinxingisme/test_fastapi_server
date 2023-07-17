from tortoise import Model, fields

from tortoise.contrib.pydantic import pydantic_model_creator




class Item(Model):
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=500)
    created_at = fields.DatetimeField(auto_now_add=True)  # auto_now_add 创建的时候更新
    updated_at = fields.DatetimeField(auto_now=True)  # auto_now 每次修改更新
    class Meta:
        table = "items"  # 指定数据库表名
        __module__ = "db.models"  # 替换为你的模块名


Item_Pydantic = pydantic_model_creator(Item)
