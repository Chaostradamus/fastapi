from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

# schema for data


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "post 1 title", "content": "content of post1", "id": 1}, {
    "title": "favorite foods", "content": "I like pizza", "id": 2
}]

# request get method url : '/'


@app.get("/")
def root():
    return {"message": "Welcome to Google foig"}


@app.get('/posts')
def get_Posts():
    return {'data': my_posts}

# decorater with post request and endpoint as /createposts


@app.post('/posts')
# path operation function called createposts that takes the variable returns as dict which is set to the body contents
# extracts body content
def create_posts(post: Post):
    print(post)
    print(post.dict())
    # returns key value pair payload[title] and payload[content] in postman
    return {"data": post}
