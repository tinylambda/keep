import functools

from fastapi import FastAPI
from fastapi.responses import \
    ORJSONResponse, \
    HTMLResponse, \
    RedirectResponse, \
    StreamingResponse, \
    FileResponse

app = FastAPI(default_response_class=ORJSONResponse)


# use ORJSONResponse for better JSON performance
@app.get('/items/', response_class=ORJSONResponse)
async def read_items():
    return [{'item_id': 'foo'}]


# return HTML response
@app.get('/items_html/', response_class=HTMLResponse)
async def read_items_html():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


@app.get('/typer')
async def redirect_typer():
    return RedirectResponse('https://www.baidu.com')


async def fake_video_streamer():
    for i in range(10):
        yield b'some fake video bytes'


@app.get('/stream')
async def stream():
    return StreamingResponse(fake_video_streamer())


@app.get('/stream_file')
async def stream_file():
    f = open('/usr/share/dict/words', 'rb')
    return StreamingResponse(iter(functools.partial(f.read, 8192), b''))


MP4_FILE = '/home/felix/Downloads/Sample-MP4-Video-File-Download.mp4'


@app.get('/stream_mp4')
def stream_mp4():
    # def iterfile():
    #     with open(MP4_FILE, 'rb') as file_like:
    #         yield from file_like
    #
    # return StreamingResponse(
    #     iterfile(),
    #     media_type='video/mp4',
    # )
    f = open(MP4_FILE, 'rb')
    return StreamingResponse(
        iter(functools.partial(f.read, 8192), b''),
        media_type='video/mp4',
    )


@app.get('/stream_mp4_async', response_class=FileResponse)
async def stream_mp4_async():
    return FileResponse(MP4_FILE, media_type='video/mp4')
