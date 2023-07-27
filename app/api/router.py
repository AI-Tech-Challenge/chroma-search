from fastapi import APIRouter 
from fastapi import File, UploadFile

from app.api.controller.search import search
from app.api.controller.root import root, submit

# cs stands for chroma-search
cs_router = APIRouter()

# root get endpoint
cs_router.add_api_route(
    "/", root, methods=["GET"],
)

# root post endpoint
cs_router.add_api_route(
    "/", submit, methods=["POST"],
)

# testing endpoint ??
cs_router.add_api_route(
    "/search", search, methods=["GET"],
)

