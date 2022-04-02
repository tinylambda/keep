from fastapi import FastAPI

app = FastAPI()

items = {}


@app.on_event('startup')
async def startup_event():
    items['foo'] = {'name': 'Fighters'}
    items['bar'] = {'name': 'Tenders'}


@app.on_event('shutdown')
async def shutdown_event():
    with open('/tmp/log.txt', 'a') as log:
        log.write('Application shutdown\n')


@app.get('/items/{item_id}')
async def read_items(item_id: str):
    return items[item_id]

# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_events:app --reload
