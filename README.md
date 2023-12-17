### Setup and run python venv

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

### Get method overview

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

