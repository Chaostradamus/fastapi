from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# schema for data

# post schema  that self validates
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "post 1 title", "content": "content of post1", "id": 1}, {
    "title": "favorite foods", "content": "I like pizza", "id": 2
}]


#                           fastapi looks at all paths and  looks for first match top to bottom



#                   loop through my_posts and if p's id matches passed in id, return it to function call
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i



#                   request get method url : '/'
 

@app.get("/")
def root():
    return {"message": "Welcome to Google foig"}

# returns as a get request
@app.get('/posts')
def get_Posts():
    return {'data': my_posts}

#               decorater with post request and endpoint as /createposts

# status_code = whatever status code you want when function runs
@app.post('/posts', status_code=status.HTTP_201_CREATED)
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



#                       get post request by ID (path parameter)

@app.get('/posts/{id}')
# fast api auto validates if id can be int and then converts
# shcema returns string for id that would need to be cast as an INT but fastapi helps us change it automatically up top 
# response variable = Response object
def get_post(id: int):
   
    # post = function call with id parameter passed in
    post = find_post(id)
    if not post:
        # one liner for below
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")
        
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f"post with id: {id} was not found"}
    print(post)
    return {"post_detail": post}



    
#               delete posts

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')

    my_posts.pop(index)
    # fast api says when you delete you shouldnt get anything back so just send response back
    return Response(status_code=status.HTTP_204_NO_CONTENT)


    #                       update
    # post is type Post so it comes in with correct schema
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    # find post and if it doesnt exist will raise error
    index = find_index_post(id)
    if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    # will take post with its detailed schema and convert to dictionary and be called post dict
    # take id of post dict
    post_dict = post.dict() 
    # set id inside new dictionary to be id passed in
    post_dict['id']  = id 
    # the post with that index will be replaced by post dict
    my_posts[index] = post_dict
    return {"data": post_dict}
   