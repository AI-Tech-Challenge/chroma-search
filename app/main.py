from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

from api.router import cs_router

app = FastAPI()

# Second endpoint (Does the search thing, used google as example. Not finished yet simplified version anyone can add to this please)
# To get this to work, run the server and input http://localhost:8000/search?q=searchterm into your explorer. Run "uvicorn main:app --reload" in the terminal first.

from fastapi import Query

# @app.get("/search")
# async def search(q: str = Query(..., description="")):
    
#     results = [
#         {"title": "Result", "description": "This is the result"},
#     ]

#     return {"results": results}

app.include_router(cs_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# to run server either type "uvicorn main:app --reload" or "python app/main.py" (assuming you're in the root directory) 

