from typing import List, Optional
from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    online: int


class User(BaseUser):
    bdate: Optional[str]


class Message(BaseModel):
    text: str
    date: int
