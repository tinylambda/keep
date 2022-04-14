import datetime

from ninja import NinjaAPI, Schema, Path

api = NinjaAPI()


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


