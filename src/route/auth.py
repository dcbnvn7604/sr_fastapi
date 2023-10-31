from typing import Any, Annotated
import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from repo.authen import Authen
from service.authen import verify_password, create_access_token, authen
from logger import logger


router = APIRouter()


class AuthCredential(BaseModel):
    email: str
    password: str


@router.post("/auth")
def auth(
    credential: AuthCredential,
    repo: Annotated[Authen, Depends()]
) -> Any:
    user = repo.user_by(credential.email)
    verified = verify_password(credential.password, user.password)
    if verified:
        token = create_access_token(user)
        return {'token': token}
    else:
        raise HTTPException(400)


@router.get("/logined")
def logined(user_id: Annotated[int, Depends(authen)]):
    pass


@router.get("/log")
def log():
    logger.info('log')
