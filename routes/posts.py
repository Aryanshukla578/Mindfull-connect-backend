from fastapi import APIRouter
from models import Post
from database import db
from bson.objectid import ObjectId

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/")
def create_post(post: Post):
    result = db.posts.insert_one(post.dict())
    return {"id": str(result.inserted_id), "status": "Post created"}

@router.get("/")
def get_posts():
    posts = list(db.posts.find())
    for p in posts:
        p["_id"] = str(p["_id"])
    return posts
