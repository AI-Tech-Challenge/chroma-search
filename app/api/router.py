from fastapi import APIRouter 

from app.api.controller.search import search
from app.api.controller.root import root

# cs stands for chroma-search
cs_router = APIRouter()

# root endpoint
cs_router.add_api_route(
    "/", root, methods=["GET"],
)

# testing endpoint ??
cs_router.add_api_route(
    "/search", search, methods=["GET"],
)

