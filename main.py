import json
from fastapi import FastAPI
from routers import blogs
from routers import books
from routers import users

app = FastAPI()
app.include_router(blogs.blog_routers)
app.include_router(books.router)
app.include_router(users.routers)

@app.get('/')
def index1():
    return 'hi there 3'