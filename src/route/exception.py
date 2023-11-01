from fastapi import APIRouter


router = APIRouter()


@router.get("/exception")
def exception():
    raise Exception()