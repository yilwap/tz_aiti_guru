from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from settings import app_settings
from view.orders import orders_router

app = FastAPI(
    title=app_settings.PROJECT_NAME,
    version=app_settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins={
        "localhost:8080",
        "127.0.0.1:8080",
    },
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders_router)
