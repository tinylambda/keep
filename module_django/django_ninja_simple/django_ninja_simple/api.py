import datetime
from typing import Optional, Any

from django.http import HttpRequest
from ninja import NinjaAPI, Schema, Path, Form
from ninja.security import django_auth, HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        if token == 'supersecret':
            return token


class GlobalAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        if token == 'supersecret':
            return token


api = NinjaAPI(csrf=True, auth=GlobalAuth())


class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return datetime.date(self.year, self.month, self.day)


@api.get('/hello')
def hello(request):
    return 'Hello, world'


@api.get('/items/{item_id}')
def read_item(request, item_id: int):
    return {'item_id': item_id}


# @api.get('/events/{year}/{month}/{day}')
# def events(request, year: int, month: int, day: int):
#     return {'date': [year, month, day]}


@api.get('/events/{year}/{month}/{day}')
def events(request, date: PathDate = Path(...)):
    return {'date': date.value()}


@api.get('/pets', auth=django_auth)
def pets(request):
    return f'Authenticated user {request.auth}'


@api.get('/bearer', auth=AuthBearer())
def bearer(request):
    return {'token': request.auth}


@api.post('/token', auth=None)
def get_token(request, username: str = Form(...), password: str = Form(...)):
    if username == 'admin' and password == '123':
        return {'token': 'supersecret'}
