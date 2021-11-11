from fastapi import FastAPI, Response, status, HTTPException
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


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if (p['id']) == id:
            return i


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(payload: Post):
    print(payload)
    print(payload.dict())

    post_dict = payload.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)

    return {"data": post_dict}


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id={id} was not found")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict

    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    print(f"Looking for post id = {id}")
    post = find_post(id)
    print(post)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id={id} was not found"
                            )

    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id={id} was not found"
                            )

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
