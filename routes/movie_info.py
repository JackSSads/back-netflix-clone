from fastapi import APIRouter
from service import GetMovieInfo

get_movie_info = GetMovieInfo()
router = APIRouter(prefix="/movie_info", tags=["movie_info"])

@router.get("/{movie_type}/{movie_id}")
async def movie_info(movie_type: str, movie_id: int):
    return await get_movie_info.get(movie_type=movie_type, movie_id=movie_id)