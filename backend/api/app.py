from http import HTTPStatus

from fastapi import FastAPI

from api.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def get_root():
    return {'message': 'Hello, World!!!'}
