## Table of Contents

- [Setup and run python venv](#setup-and-run-python-venv)
- [Get method overview](#get-method-overview)
- [Operation description](#operation-description)
- [Routers](#routers)

## Setup and run python venv

1. make a folder for example : 

```
mkdir fastapi-practice

// change the directory

cd fastapi-practice 

```
2. Create a python vertual entvirontment

```
python -m venv fastapi-venv

// now active the entvironement

source fastapi-venv/bin/active

// install fastAPI and uvicorn using pip

pip install fastapi

pip install uvicorn

```

3. Open your project in vscode and run these command

```
source fastapi-venv/bin/active

// run the uvicorn server 

uvicorn main:app --reload
```

## Get method overview

1. path parameters
```python
@app.get('/blog/{id}')
def index(id):
    return f'This is blog with id {id}'
```
2. Predefined values
Predefined values with Enum
```python
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return f'blog type is {type}'
```
3. Query parameters
```python
@app.get('/blog/all')
def get_all_blog(page = 1, page_size = 100):
    return f'All blog from {page} and {page_size} rovided!'
```
4. Path and Query parameters
```python
@app.get('/blog/{id}/comments/{comment_id}')
def get_blog_with_comments_id(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return f'Blog id {id}, comment id {comment_id}, valid { valid}, username {username}'
```
## Operation description

http Status code.
We can send back status code if something not found.
```python
@app.get('/book/{id}', status_code=status.HTTP_404_NOT_FOUND)
def get_book(id: int):
    if id > 7:
        return f'Book is not found!'
    else:
        return f'Book id is {id}'
```
We can also change the status code on the response.
```python
@app.get('/book/{id}', status_code=status.HTTP_200_OK)
def get_book(id: int, response: Response):
    if id > 7:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f'Book is not found!'
    else:
        response.status_code = status.HTTP_200_OK
        return f'Book id is {id}'
```
We can use tags to categorize our operations, summary , description, response_description
```python
@app.get('/blog/all', tags=['blog'])

@app.get('/book/{id}', status_code=status.HTTP_200_OK, tags=['Books'])

@app.get('/book/{id}', status_code=status.HTTP_200_OK,
         tags=['Books'],
         summary='This is our single book route',
         description='This route responsible for fetch book and update book',
         response_description='Response to get book'
        )
```
## Routers
Using routers we can separate operations into multiple files.

```python
// routers/blogs.py
blog_routers = APIRouter(
    prefix='/blog',
    tags=['blog']
)

""" Query parameters with Default values """
@blog_routers.get('/all')
def get_all_blog(page = 1, page_size = 100):
    return f'All blog from {page} and {page_size} provided!'

// main.py
app = FastAPI()
app.include_router(blogs.blog_routers)

```
