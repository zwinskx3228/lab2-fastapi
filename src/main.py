from fastapi import FastAPI

from src.core.router import router as common_router
from src.storage.router import router as storage_router

app = FastAPI(
    title="Azure FastAPI Lab",
    description="FastAPI application integrated with Azure Blob Storage",
    version="1.0.0"
)

app.include_router(common_router)
app.include_router(storage_router)