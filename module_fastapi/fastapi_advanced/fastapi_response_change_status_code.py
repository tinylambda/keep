from fastapi import FastAPI, status
from fastapi.responses import Response

app = FastAPI()

tasks = {"foo": "Listen to the Bar Fighters"}


@app.put('/get-or-create-task/{task_id}', status_code=status.HTTP_200_OK)
def get_or_create_task(task_id: str, response: Response):
    if task_id not in tasks:
        tasks[task_id] = 'This did not exist before'
        response.status_code = status.HTTP_201_CREATED
    return tasks[task_id]

# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_response_change_status_code:app --reload
