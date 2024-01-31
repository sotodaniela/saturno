from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path



app = FastAPI()

#templates = Jinja2Templates(directory="templates")
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

@app.get("/pagina")
def mostrar_pagina(request: Request):
    message = "¡Hola desde FastAPI!"
    return templates.TemplateResponse("index.html", {"request": request, "message": message})

#@app.get("/")
#def read_root():
 #   return {"Hello": "World"}


BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))