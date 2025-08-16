from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get('/')
def index():
	return {'data': {'name':'vani'}}

@app.get('/blog/{id}')
def show(id):
    return f'{id}'

class Blog(BaseModel):
    title:str
    body:str

@app.post('/blog')
def create_blog(request:Blog):
    return request


