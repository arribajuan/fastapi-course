from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from pydantic.types import OptionalInt


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: OptionalInt = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your list of posts"}


@app.post("/posts")
def post_posts(payload: Post):
    print(payload)
    return {"new_post": f"title: '{payload.title}',  content: '{payload.content}', published: '{payload.published}', rating: '{payload.rating}'"}
