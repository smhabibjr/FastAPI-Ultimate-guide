from fastapi import FastAPI

app = FastAPI()

@app.get('/new')
def index():
    return {'msg': 'hello world'}
