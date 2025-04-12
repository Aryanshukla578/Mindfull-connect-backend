from fastapi import APIRouter
from pydantic import BaseModel
from database import db
from bson.objectid import ObjectId
from typing import List, Optional

router = APIRouter(prefix="/resources", tags=["Resources"])

class Resource(BaseModel):
    title: str
    description: str
    link: Optional[str] = None
    tags: Optional[List[str]] = []

@router.post("/")
def add_resource(resource: Resource):
    result = db.resources.insert_one(resource.dict())
    return {"id": str(result.inserted_id), "status": "Resource added"}

@router.get("/")
def list_resources():
    resources = list(db.resources.find())
    for res in resources:
        res["_id"] = str(res["_id"])
    return resources
