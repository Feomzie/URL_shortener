from fastapi import FastAPI
from app.core.routes.url import router

app = FastAPI(title="URL Shortener")

app.include_router(router)