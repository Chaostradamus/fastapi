from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



# schema for data

# post schema  that self validates
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='postgres', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful!")
        break
    # catch block exception will be stored as error
    except Exception as error:
        print('connection failed')
        print("Error:", error)
        time.sleep(2)


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


@app.get("/sqlalchemy")
# pass in db and itll make it a dependency. must pass in to work with database in the path operation

def test_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    print(posts)
    return {"data": posts}

                            # returns as a get request
@app.get('/posts')
def get_posts(db: Session = Depends(get_db)):
    # sql commands raw code to get stuff
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {'data': posts}

#               decorater with post request and endpoint as /createposts



# status_code = whatever status code you want when function runs
@app.post('/posts', status_code=status.HTTP_201_CREATED)
# path operation function called createposts that takes the variable returns as dict which is set to the body contents
# extracts body content
def create_posts(post: Post, db: Session = Depends(get_db)):
#    sql code for creating posts
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    
    new_post = models.Post(
        **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}



#                       get post request by ID (path parameter)

@app.get('/posts/{id}')
# fast api auto validates if id can be int and then converts
# shcema returns string for id that would need to be cast as an INT but fastapi helps us change it automatically up top 
# response variable = Response object
def get_post(id: int):
    # use cursor object to run sql commands
    cursor.execute("""SELECT * from posts where id = %s""", (str(id)))
    post = cursor.fetchone()
  
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
    cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit() 
    
   
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')

    # fast api says when you delete you shouldnt get anything back so just send response back
    return Response(status_code=status.HTTP_204_NO_CONTENT)


    #                       update
    # post is type Post so it comes in with correct schema
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
     (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    # find post and if it doesnt exist will raise error
    
    if updated_post == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    
    return {"data": updated_post}
   