from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

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


#                           fastapi looks at all paths and  looks for first match top to bottom



# loop through my_posts and if p's id matches passed in id, return it to function call
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# request get method url : '/'


@app.get("/")
def root():
    return {"message": "Welcome to Google foig"}

# returns as a get request
@app.get('/posts')
def get_Posts():
    return {'data': my_posts}

# decorater with post request and endpoint as /createposts


@app.post('/posts')
# path operation function called createposts that takes the variable returns as dict which is set to the body contents
# extracts body content
def create_posts(post: Post):
    # post pydantic model converted to a dictionary
    post_dict = post.dict()
# post dict targeting ID field set to some random #
    post_dict['id'] = randrange(0, 1000000)
    # append to array
    my_posts.append(post_dict)
    # returns key value pair payload[title] and payload[content] in postman
    return {"data": post_dict}

# get post request by ID (path parameter)

@app.get('/posts/{id}')
# fast api auto validates if id can be int and then converts
# shcema returns string for id that would need to be cast as an INT but fastapi helps us change it automatically up top 
def get_post(id: int):
   
    # post = function call with id parameter passed in
    post = find_post(id)
    print(post)
    return {"post_detail": post}