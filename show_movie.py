from movie.movie import list, show_time


# Main program
if __name__ == "__main__":
    movie_name = input("Enter the movie name: ")
    res = list(movie_name)
    print(res.status_code)
    print(res.json())
