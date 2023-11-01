from fastapi import APIRouter

from logger import logger


router = APIRouter()


@router.get("/log")
def log():
    logger.info('log')
