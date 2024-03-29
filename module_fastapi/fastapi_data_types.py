import uuid
from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import FastAPI, Body, Path

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID = Path(..., example=uuid.uuid4()),
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None, example=timedelta(hours=1)),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


# PYTHONPATH=module_fastapi uvicorn fastapi_data_types:app --reload
