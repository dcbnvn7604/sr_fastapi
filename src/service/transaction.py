from typing import Annotated
from fastapi import Depends

from repo.transaction import Transaction as Repo
from db.database import transaction


class Transaction:
    def __init__(self, repo: Annotated[Repo, Depends()]):
        self.repo = repo
        self.db = repo.db
    
    @transaction
    def fail_multiple(self):
        self.repo.add_user1()
        self.repo.add_user2()
        raise Exception('fail_multiple')