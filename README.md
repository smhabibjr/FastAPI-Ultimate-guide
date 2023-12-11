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
3. Query parameters

