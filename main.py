from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index1():
    return 'hi htere 3'

@app.get('/blog/all')
def get_all_blog():
    return 'All blog provided!'

@app.get('/blog/{id}')
def blog(id: int):
    return f'This is blog with id {id}'

