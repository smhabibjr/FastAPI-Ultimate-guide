from fastapi import APIRouter, Response, status

router = APIRouter(
    prefix='/book',
    tags=['book']
)

@router.get('/book/{id}', status_code=status.HTTP_200_OK,
         summary='This is our single book route',
         description='This route responsible for fetch book and update book',
         response_description='Response to get book'
        )

def get_book(id: int, response: Response):
    if id > 7:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f'Book is not found!'
    else:
        response.status_code = status.HTTP_200_OK
        return f'Book id is {id}'