from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.api.router import cs_router

app = FastAPI()

app.include_router(cs_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

# to run server either type "uvicorn main:app --reload" or "python app/main.py" (assuming you're in the root directory) 
# test
