from fastapi import Depends
from typing import Annotated, Any


from db.model import User
from db.database import get_db

class Authen:
    def __init__(self, db: Annotated[Any, Depends(get_db)]):
        self.db = db
    
    def user_by(self, email) -> User :
        return self.db.query(User) \
            .filter(User.email == email) \
            .one()
