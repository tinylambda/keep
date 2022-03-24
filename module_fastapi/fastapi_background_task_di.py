from typing import Optional

from fastapi import FastAPI, BackgroundTasks, status, Query, Depends

app = FastAPI()


def write_log(message: str):
    with open('/tmp/log.txt', 'a') as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f'found query: {q}\n'
        background_tasks.add_task(write_log, message)
    return q


@app.post('/send-notification/{email}', status_code=status.HTTP_202_ACCEPTED)
async def send_notification(email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)):
    message = f'message to {email}\n'
    background_tasks.add_task(write_log, message)
    return {'message': 'Message sent'}

# PYTHONPATH=module_fastapi uvicorn fastapi_background_task_di:app --reload
