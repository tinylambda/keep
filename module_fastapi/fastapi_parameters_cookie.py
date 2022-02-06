from typing import Optional

from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get('/items')
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {'ads_id': ads_id}


# PYTHONPATH=module_fastapi uvicorn fastapi_parameters_cookie:app --reload
# Note: We should create a Cookie in browser and visit the URL in a new browser tab
# See https://github.com/tiangolo/fastapi/issues/880
