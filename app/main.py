from fastapi import FastAPI
import uvicorn

from api.router import cs_router

app = FastAPI()

app.include_router(cs_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# to run server either type "uvicorn main:app --reload" or "python app/main.py" (assuming you're in the root directory) 

