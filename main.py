from fastapi import FastAPI
from apis.routes import router as api_router
from services.routes import router as service_router
from tortoise.contrib.fastapi import register_tortoise
# from config.dbconfig import db_username, db_password, db_host, db_port, db_name

import uvicorn

app = FastAPI()

DATABASE_URL = "sqlite:///./app.db"
# DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

register_tortoise(app,
                  db_url=DATABASE_URL,
                  modules={"models": ['db.models']},
                  add_exception_handlers=True,
                  generate_schemas=True)

app.include_router(api_router, prefix="/api")
# app.include_router(service_router, prefix="/service")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
