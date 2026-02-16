from fastapi.responses import FileResponse
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="My Forum API",
    description="API for small forum",
    version="1.0.0"
)
front_dir = os.path.join(os.path.dirname(__file__), '..', 'front')
app.mount('/static', StaticFiles(directory=front_dir), name="static")

@app.get('/')
def read_index():
    html_path = os.path.join(front_dir, "forum.html")
    return FileResponse(html_path)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)