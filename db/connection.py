from tortoise.contrib.fastapi import register_tortoise
from config.dbconfig import db_username, db_password, db_host, db_port, db_name
from main import app

# DATABASE_URL = "sqlite:///./app.db"
DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = register_tortoise(app,
                           DATABASE_URL,
                           modules={"models": ['db.models']},
                           add_exception_handlers=True,
                           generate_schemas=True)
