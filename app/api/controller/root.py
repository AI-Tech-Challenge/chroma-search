from fastapi.templating import Jinja2Templates
from fastapi import Request, Form

templates = Jinja2Templates(directory="templates")

async def root(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})

async def submit(req: Request, user_input: str=Form(...)):
    print(user_input)
    return templates.TemplateResponse("index.html", {"request": req, "user_input": user_input})