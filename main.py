from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from os import getenv

load_dotenv()

from service import GetMovies, GetMovieInfo

app = FastAPI()
get_movie = GetMovies()
get_movie_info = GetMovieInfo()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[getenv("URL_FRONTEND")],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Origin", "X-Requested-With", "Content-Type", "Accept"],
)

@app.get("/")
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

@app.get("/movie_info/{movie_type}/{movie_id}")
async def movie_info(movie_type: str, movie_id: int):
    return await get_movie_info.get(movie_type=movie_type, movie_id=movie_id)
    