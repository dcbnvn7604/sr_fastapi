from fastapi import FastAPI, Request
import uuid

from route import auth
from logger import request_id, logger

app = FastAPI()

app.include_router(auth.router)

@app.middleware("http")
async def log_request(request: Request, call_next):
    request_id.set(str(uuid.uuid4()))
    parameters = {
        'path': request.url.path
    }
    logger.info(f'Parameter {parameters}')
    response = await call_next(request)
    logger.info(f'Status {response.status_code}')
    return response
