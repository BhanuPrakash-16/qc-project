from fastapi import APIRouter
from .. import schemas, crud

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/", response_model=schemas.MovieResponse)
async def add_movie(movie: schemas.MovieCreate):
    return await crud.add_movie(movie)

@router.get("/")
async def get_movies():
    return await crud.list_movies()
