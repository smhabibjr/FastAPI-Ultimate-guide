from typing import Optional
from fastapi import APIRouter, Response, status
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
    published: Optional[bool]   

@blog_routers.post('/new')
def create_blog(item : BlogPost):
    # Logic to create the blog
    return { 'message': f'Blog has been successfully created', 'item': item }


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