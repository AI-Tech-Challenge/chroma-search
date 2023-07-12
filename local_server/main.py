from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# First endpoint
@app.get("/")
async def root():
    return "Chroma Search"

# Second endpoint (Does the search thing, used google as example. Not finished yet simplified version anyone can add to this please)
# To get this to work, run the server and input http://localhost:8000/search?q=searchterm into your explorer. Run "uvicorn main:app --reload" in the terminal first.
@app.get("/search")
async def search(q: str = Query(..., description="")):
    
    results = [
        {"title": "Result", "description": "This is the result"},
    ]

    return {"results": results}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

