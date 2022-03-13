from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

"""
If you declare the type of your path operation function parameter as bytes, 
FastAPI will read the file for you and you will receive the contents as bytes.

Have in mind that this means that the whole contents will be stored in memory. This will work well for small files.
"""


@app.post('/file/')
async def create_file(file: bytes = File(..., description='read as bytes')):
    return {'file_size': len(file)}


@app.post('/uploadfile/')
async def create_upload_file(file: UploadFile = File(..., description='read as UploadFile')):
    return {'filename': file.filename}


@app.post('/files/')
async def create_files(files: List[bytes] = File(...)):
    return {'file_sizes': [len(file) for file in files]}


@app.post('/uploadfiles/')
async def create_upload_files(files: List[UploadFile]):
    return {'filenames': [file.filename for file in files]}


@app.get('/')
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


# PYTHONPATH=module_fastapi uvicorn fastapi_request_form_file:app --reload
