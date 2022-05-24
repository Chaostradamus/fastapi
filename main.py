from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# request get method url : '/'

@app.get("/")
def root():
    return {"message": "Welcome to Google foig"}

@app.get('/posts')
def get_Posts():
    return {'data': 'this is the post'}

@app.post('/createposts')
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}