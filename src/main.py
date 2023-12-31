from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uuid

from route import auth, exception, log, transaction
from logger import request_id, logger

app = FastAPI()

app.include_router(auth.router)
app.include_router(exception.router)
app.include_router(log.router)
app.include_router(transaction.router)

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


@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={})
