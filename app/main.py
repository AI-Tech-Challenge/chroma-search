from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

from app.api.router import cs_router

app = FastAPI()

app.include_router(cs_router)
app.mount (
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# to run server:
# first make sure you're in the root directory (important)
# type "uvicorn app.main:app --reload" 
