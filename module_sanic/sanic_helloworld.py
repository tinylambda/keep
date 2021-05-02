from sanic import Sanic
from sanic.response import text


app = Sanic("my hello world app")


@app.get('/')
async def hello_world(request):
    return text('hello world')

