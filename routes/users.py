from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from database import db
from bson.objectid import ObjectId

router = APIRouter(prefix="/users", tags=["Users"])

class User(BaseModel):
    username: str
    email: Optional[str] = None
    anonymous: bool = False

@router.post("/")
def create_user(user: User):
    result = db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id), "status": "User created"}

@router.get("/{user_id}")
def get_user(user_id: str):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return user
    return {"error": "User not found"}
