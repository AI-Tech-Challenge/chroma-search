from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

templates = Jinja2Templates(directory="app/templates")

async def root(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})
