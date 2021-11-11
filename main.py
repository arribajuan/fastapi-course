from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from pydantic.types import OptionalInt
from random import randrange


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: OptionalInt = None


# Temporary, in-memory database
my_posts = [
    {"title": "title 1", "content": "content 1", "id": 1},
    {"title": "title 2", "content": "content 2", "id": 2},
    {"title": "title 3", "content": "content 3", "id": 3},
]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def post_posts(payload: Post):
    print(payload)
    print(payload.dict())

    post_dict = payload.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)

    return {"data": post_dict}
