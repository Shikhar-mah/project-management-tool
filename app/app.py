from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_table, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_table()
    yield

app = FastAPI()

text_post = {
    1: {"Title": "New Post", "content": "cool test post"},
    2: {"Title": "Morning Thoughts", "content": "Starting the day with coffee and a bit of coding."},
    3: {"Title": "Debugging Mode", "content": "Spent the afternoon fixing a bug that turned out to be a missing comma."},
    4: {"Title": "Quick Update", "content": "Just pushed a small update to improve performance."},
    5: {"Title": "Learning Python", "content": "Practicing dictionaries and loops today."},
    6: {"Title": "Random Idea", "content": "Thinking about building a simple API for testing."},
    7: {"Title": "Late Night Coding", "content": "Nothing beats writing code when everything is quiet."},
    8: {"Title": "Testing Post", "content": "This is another dummy entry used for testing purposes."},
    9: {"Title": "Mini Project", "content": "Working on a small side project to improve backend skills."},
    10: {"Title": "Notes", "content": "Remember to refactor the authentication module later."},
    11: {"Title": "Code Review", "content": "Reviewed some code and found a few improvements."},
    12: {"Title": "Experiment", "content": "Trying out a different data structure today."},
    13: {"Title": "Feature Idea", "content": "Maybe add search functionality in the next version."},
    14: {"Title": "Progress Log", "content": "Completed most of the core logic for the app."},
    15: {"Title": "Weekend Coding", "content": "Spent some time experimenting with APIs."},
    16: {"Title": "Final Test Entry", "content": "Last dummy post entry for testing the dataset."}
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_post.values())[:limit]
    return text_post

@app.get("/posts/{id}")
def fetch_post_by_id(id: int):
    if id not in text_post:
        return HTTPException(status_code=404, detail="Post not found")

    return text_post.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_post[max(text_post.keys()) + 1] = new_post
    return new_post