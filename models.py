from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    username: str
    email: Optional[str]
    anonymous: bool = False

class Post(BaseModel):
    user_id: str
    content: str
    tags: Optional[List[str]] = []
