from curses import version
from typing import Optional
from fastapi import APIRouter, Query
from enum import Enum

from pydantic import BaseModel

blog_routers = APIRouter(
    prefix='/blog',
    tags=['blog']
)

""" Query parameters with Default values """
@blog_routers.get('/all')
def get_all_blog(page = 1, page_size = 100):
    return f'All blog from {page} and {page_size} provided!'

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    published: Optional[bool]   

@blog_routers.post('/new/{id}')
def create_blog(blog : BlogPost, id: int = 1111, version: int = 1.0):
    print(blog.title)
    return {'id': id, 'version':version, 'data': blog}

@blog_routers.post('/new/{id}/comments')
def create_blog_with_comments(
    blog : BlogPost, 
    id: int,
    comments_id: int = Query(None,
                    title='Blog id',
                    description='This is blog id',
                    alias='blog-id')):

    return {'id': id, 'data': blog}

""" Predefined values """
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@blog_routers.get('/type/{type}')
def get_blog_type(type: BlogType):
    return f'blog type is {type}'

""" path parameters example """
@blog_routers.get('/{id}')
def blog(id: int):
    return f'This is blog with id {id}'

@blog_routers.get('/{id}/comments/{comment_id}')
def get_blog_with_comments_id(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return f'Blog id {id}, comment id {comment_id}, valid { valid}, username {username}'