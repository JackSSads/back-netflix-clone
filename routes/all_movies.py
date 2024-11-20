from fastapi import APIRouter
from service import GetMovies

router = APIRouter()
get_movie = GetMovies()

@router.get("/", tags=["all_movies"])

async def all_movies():
    res = [
        {
            "slug": "originals",
            "title": "Originais Netflix",
            "items": await get_movie.originals()
        },
        {
            "slug": "trending",
            "title": "Recomendados para você",
            "items": await get_movie.trending()
        },
        {
            "slug": "toprated",
            "title": "Em Alta",
            "items": await get_movie.toprated()
        },
        {
            "slug": "action",
            "title": "Ação",
            "items": await get_movie.action()
        },
        {
            "slug": "comedy",
            "title": "Comédia",
            "items": await get_movie.comedy()
        },
        {
            "slug": "horror",
            "title": "Horror",
            "items": await get_movie.horror()
        },
        {
            "slug": "romance",
            "title": "Romance",
            "items": await get_movie.romance()
        },
        {
            "slug": "documentary",
            "title": "Documentário",
            "items": await get_movie.documentary()
        }
    ]

    return res