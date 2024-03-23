from movie.requestor import Requestor

class Movie:
    def __init__(self, title: str, year: int = None, country_of_origin: str = None):
        self.title = title
        self.year = year
        self.country_of_origin = country_of_origin

    @classmethod
    def from_title(cls, title: str) -> Movie:
        pass


def list(name:str):
    """Searches for a movie by title and returns a list of movies that match the search term."""
    requestor = Requestor()
    return requestor.request("GET", "/v2/movies/views/now-playing", params={"name": name})

def show_time(id:str):
    """Returns a list of showtimes for a movie."""
    pass

