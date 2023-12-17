from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
def index1():
    return 'hi htere 3'

""" path parameters example """
""" @app.get('/blog/all')
def get_all_blog():
    return 'All blog provided!' """

""" Query parameters with Default values """
@app.get('/blog/all')
def get_all_blog(page = 1, page_size = 100):
    return f'All blog from {page} and {page_size} provided!'

""" Predefined values """
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return f'blog type is {type}'

""" path parameters example """
@app.get('/blog/{id}')
def blog(id: int):
    return f'This is blog with id {id}'

@app.get('/blog/{id}/comments/{comment_id}')
def get_blog_with_comments_id(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return f'Blog id {id}, comment id {comment_id}, valid { valid}, username {username}'