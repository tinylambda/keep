from typing import Optional, List

from fastapi import FastAPI, Header

app = FastAPI()


@app.get('/items')
async def read_items(user_agent: Optional[str] = Header(None, convert_underscores=True)):
    return {'User-Agent': user_agent}


@app.get('/items2')
async def read_items2(x_token: Optional[List[str]] = Header(None)):
    return {'X-Token values': x_token}


# Before setting convert_underscores to False,
# bear in mind that some HTTP proxies and servers disallow the usage of headers with underscores.

# PYTHONPATH=module_fastapi uvicorn fastapi_parameters_header:app --reload
