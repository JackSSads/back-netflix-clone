from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from os import getenv

from routes import all_movies_router, movie_info_router

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[getenv("URL_FRONTEND")],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Origin", "X-Requested-With", "Content-Type", "Accept"],
)

app.include_router(all_movies_router)
app.include_router(movie_info_router)

if __name__ == "__main__":
        run(app, host="0.0.0.0", port=8001)