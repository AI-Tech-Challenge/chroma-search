from fastapi import Query

async def search(q: str = Query(..., description="")):
    
    results = [
        {"title": "Result", "description": "This is the result"},
    ]

    return {"results": results}
