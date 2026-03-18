from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from checker import check_password

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
def check(request: Request, password: str = Form(...)):
    result = check_password(password)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result, "password": password}
    )