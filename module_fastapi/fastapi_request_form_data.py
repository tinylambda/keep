from fastapi import FastAPI, Form

app = FastAPI()


"""
Data from forms is normally encoded using the "media type" application/x-www-form-urlencoded.

But when the form includes files, it is encoded as multipart/form-data. 
You'll read about handling files in the next chapter.
"""


@app.post('/login/')
async def login(username: str = Form(...), password: str = Form(...)):
    return {'username': username}

# PYTHONPATH=module_fastapi uvicorn fastapi_request_form_data:app --reload
