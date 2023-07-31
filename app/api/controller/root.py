from fastapi.templating import Jinja2Templates
from fastapi import Request, Form

from app.core.generate_hexcodes import generate_hexcodes

templates = Jinja2Templates(directory="templates")

async def root(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})

async def submit(req: Request, user_input: str=Form(...)):
    hexcodes = generate_hexcodes(user_input)
    return templates.TemplateResponse("index.html", {"request": req, "user_input": hexcodes})