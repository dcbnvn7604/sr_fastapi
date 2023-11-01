from typing import Annotated, Any
from fastapi import Depends

from db.database import get_db, transaction
from db.model import User


class Transaction:
    def __init__(self, db: Annotated[Any, Depends(get_db)]) -> None:
        self.db = db
    
    @transaction
    def add_user1(self):
        user = User(email='email1@example.com', password='password1')
        self.db.add(user)
    

    @transaction
    def add_user2(self):
        user = User(email='email2@example.com', password='password2')
        self.db.add(user)