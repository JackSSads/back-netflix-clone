import httpx
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class HTTPRequest:
    def __init__(self):
        self.__api_base = getenv("API_BASE")
        self.__api_key = getenv("API_KEY")
        self.__headers = {"accept": "application/json"}
    
    async def get(self, endpoint: str, params: dict = None):
        try:
            url = f"{self.__api_base}{endpoint}"

            params["api_key"] = self.__api_key

            async with httpx.AsyncClient() as client:
                req = await client.get(url, headers=self.__headers, params=params)
                req.raise_for_status()
                return req.json()

        except httpx.RequestError as e:
            return {"error": str(e)}

class GetMovies:
    # TODO Mover a chave da api para o .env

    def __init__(self):
        self.http = HTTPRequest()

    async def originals(self):
        return await self.http.get("/discover/tv", {"with_network": 213, "language": "pt-BR"}) 
    
    async def trending(self):
        return await self.http.get("/trending/all/week", {"language": "pt-BR"})
           
    async def toprated(self):
        return await self.http.get("/movie/top_rated", {"language": "pt-BR"})

    async def action(self):
        return await self.http.get("/discover/movie", {"with_genres": 28, "language": "pt-BR"})
            
    async def comedy(self):
        return await self.http.get("/discover/movie", {"with_genres": 35, "language": "pt-BR"})

    async def horror(self):
        return await self.http.get("/discover/movie", {"with_genres": 27, "language": "pt-BR"})
           
    async def romance(self):
        return await self.http.get("/discover/movie", {"with_genres": 10749, "language": "pt-BR"})

    async def documentary(self):
        return await self.http.get("/discover/movie", {"with_genres": 99, "language": "pt-BR"})
             
class GetMovieInfo:
    def __init__(self):
        self.http = HTTPRequest()

    async def get(self, movie_type: str, movie_id: int):
        return await self.http.get(f"/{movie_type}/{movie_id}", {"language": "pt-BR"})
    

