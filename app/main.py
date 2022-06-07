from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings





# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to Google foig"}













#                   request get method url : '/'
 

# @app.get("/")
# def root():
#     return {"message": "Welcome to Google foig"}



#                             # returns as a get request
# @app.get('/posts', response_model=List[schemas.Post])
# def get_posts(db: Session = Depends(get_db)):
#     # sql commands raw code to get stuff
#     # cursor.execute("""SELECT * FROM posts""")
#     # posts = cursor.fetchall()
#     posts = db.query(models.Post).all()
#     return posts

# #               decorater with post request and endpoint as /createposts



# # status_code = whatever status code you want when function runs
# @app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# # path operation function called createposts that takes the variable returns as dict which is set to the body contents
# # extracts body content
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
# #    sql code for creating posts
#     # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
#     # new_post = cursor.fetchone()
#     # conn.commit()
    
    
#     new_post = models.Post(
#         **post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post



# #                       get post request by ID (path parameter)

# @app.get('/posts/{id}', response_model=schemas.Post)
# # fast api auto validates if id can be int and then converts
# # shcema returns string for id that would need to be cast as an INT but fastapi helps us change it automatically up top 
# # response variable = Response object
# def get_post(id: int, db: Session = Depends(get_db)):
#     # use cursor object to run sql commands
#     # cursor.execute("""SELECT * from posts where id = %s""", (str(id)))
#     # post = cursor.fetchone()
  
#     post = db.query(models.Post).filter(models.Post.id == id).first()
    
    
#     if not post:
#         # one liner for below
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"post with id: {id} was not found")
        
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'message': f"post with id: {id} was not found"}
#     print(post)
#     return post



    
# #               delete posts

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     # cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id),))
#     # deleted_post = cursor.fetchone()
#     # conn.commit() 
    
#     post = db.query(models.Post).filter(models.Post.id == id)


#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')
#     post.delete(synchronize_session=False)
#     db.commit()
#     # fast api says when you delete you shouldnt get anything back so just send response back
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


#     #                       update
#     # post is type Post so it comes in with correct schema
# @app.put("/posts/{id}", response_model=schemas.Post)
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
#     #  (post.title, post.content, post.published, str(id)))
#     # updated_post = cursor.fetchone()
#     # conn.commit()
#     # find post and if it doesnt exist will raise error
    
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     post = post_query.first()

#     if post == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     post_query.update(updated_post.dict(), synchronize_session=False)
#     db.commit()

#     return post_query.first()

#     #                                   USER DATABASE


# @app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# # pydantic model usercreate stored as user
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password


#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/users/{id}', response_model=schemas.UserOut)
# # extract ID and validate as int
# def get_user(id: int, db: Session = Depends(get_db), ):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")
#     return user
