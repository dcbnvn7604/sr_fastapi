from fastapi import FastAPI

from route import auth

app = FastAPI()

app.include_router(auth.router)