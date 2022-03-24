from fastapi import FastAPI, status
from starlette.background import BackgroundTasks

app = FastAPI()


def write_notification(email: str, message=''):
    with open('/tmp/log.txt', mode='a') as email_file:
        content = f'notification for {email}: {message}'
        email_file.write(content)


@app.post('/send-notification/{email}', status_code=status.HTTP_202_ACCEPTED)
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message='I am fine.')
    return {'message': 'Notification sent in the background'}

# PYTHONPATH=module_fastapi uvicorn fastapi_background_task:app --reload
