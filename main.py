from fastapi import FastAPI
from .apis.routes import router as api_router
from .services.routes import router as service_router
from .db.connection import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(api_router, prefix="/api")
app.include_router(service_router, prefix="/service")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
