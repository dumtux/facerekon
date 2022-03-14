from contextlib import closing
from datetime import datetime
import os
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from facerekon.config import (
	__title__,
	__description__,
	__version__,
	IMAGES_NAMED,
	IMAGES_UNNAMED,
	STATIC,
)
from facerekon.compare import compare_face


app = FastAPI(title=__title__, description=__description__, version=__version__,)
app.mount("/api/download/named", StaticFiles(directory=IMAGES_NAMED), name="named")
app.mount("/api/download/unnamed", StaticFiles(directory=IMAGES_UNNAMED), name="unnamed")


@app.get("/")
async def root():
    return FileResponse(os.path.join(STATIC, 'index.html'))


@app.post('/api/upload/named')
async def named(files: List[UploadFile] = File(...)):
    names = []
    for file in files:
        save_to_named(file)
        names.append(file.filename)
    return {
        'msg': 'saved',
        'files': names
    }


@app.post('/api/upload/unnamed')
async def unnamed(files: List[UploadFile] = File(...)):
    result = []
    for file in files:
        tmp_file = save_to_unnamed(file)
        match = await compare_face(tmp_file, IMAGES_NAMED)
        result.append({
            'msg': 'named',
            'original': file.filename,
            'proposed': match
        })
    return result


def save_to_named(file: UploadFile):
    tmp_file = os.path.join(IMAGES_NAMED, file.filename)
    with closing(open(tmp_file, 'wb')) as f:
        f.write(file.file.read())


def save_to_unnamed(file: UploadFile) -> str:
    # d = datetime.now()
    # fname = str(hash(d) & 0xffffffff) + ' ' + str(d)
    # fname +='.' + file.filename.split('.')[-1]
    # fname = fname.replace(' ', '_')
    fname = file.filename
    tmp_file = os.path.join(IMAGES_UNNAMED, fname)
    with closing(open(tmp_file, 'wb')) as f:
        f.write(file.file.read())

    return tmp_file
