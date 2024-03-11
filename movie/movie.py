from movie.requestor import Requestor

class Movie:
    def __init__(self, title, year, imdb_id):
        self.title = title
        self.year = year
        self.imdb_id = imdb_id

def list(name:str):
    """Searches for a movie by title and returns a list of movies that match the search term."""
    requestor = Requestor()
    return requestor.request("GET", "/v2/movies/views/now-playing", params={"name": name})

def show_time(id:str):
    """Returns a list of showtimes for a movie."""
    pass

