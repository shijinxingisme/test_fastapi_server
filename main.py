from fastapi import FastAPI
from apis.routes import router as api_router
from services.routes import router as service_router
from tortoise.contrib.fastapi import register_tortoise
# from config.dbconfig import db_username, db_password, db_host, db_port, db_name
import os
from pathlib import Path

import uvicorn

app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "app.db"
if not DATABASE_FILE.exists():
    DATABASE_FILE.touch()

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"
# DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

register_tortoise(app,
                  db_url=DATABASE_URL,
                  modules={"models": ['db.models']},
                  add_exception_handlers=True,
                  generate_schemas=True)

app.include_router(api_router, prefix="/api")
app.include_router(service_router, prefix="/service")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
