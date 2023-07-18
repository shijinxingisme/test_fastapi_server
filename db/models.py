from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Item(Model):
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=500)
    created_at = fields.DatetimeField(auto_now_add=True)  # auto_now_add 创建的时候更新
    updated_at = fields.DatetimeField(auto_now=True)  # auto_now 每次修改更新


# 使用pydantic_model_creator创建Pydantic模型
ItemPydantic = pydantic_model_creator(Item, name="ItemPydantic")
