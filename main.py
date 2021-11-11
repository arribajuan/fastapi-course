from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your list of posts"}


@app.post("/posts")
def post_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: '{payload['title']}'',  content: '{payload['content']}'"}
