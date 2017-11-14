"""Defines the Movie class that contains the details of a movie."""
import webbrowser


# self is object of class movie share it to object call it
"""This class provides a way to store movie related information.
   Attributes:
       title: A string to store the title of the movie.
       storyline: A string to store the basic plot of the movie.
       poster_image_url: A string to store the URL of the movie poster.
       trailer_youtube_url: A string to store the URL of the movie trailer.
       release_date: A string to store the release date of the movie.
   """


class Movie():


    def __init__(self, movie_title, movie_story, poster_img, trailer_youtube):
        self.title = movie_title
        # title of filme
        self.storyline = movie_story
        # storyline of filme
        self.poster_image_url = poster_img
        # poster of filme
        self.trailer_youtube_url = trailer_youtube
        # url filme from youtube

    # if Remove self convert into local_var can't access it from any file
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
