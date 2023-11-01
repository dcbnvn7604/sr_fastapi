from fastapi import APIRouter, Depends
from typing import Annotated

from repo.transaction import Transaction
from service.transaction import Transaction as TransactionSvc


router = APIRouter()


@router.get("/transaction/single")
def transaction_single(repo: Annotated[Transaction, Depends()]):
    repo.add_user1()


@router.get("/transaction/multiple")
def transaction_multiple(service: Annotated[TransactionSvc, Depends()]):
    service.fail_multiple()
