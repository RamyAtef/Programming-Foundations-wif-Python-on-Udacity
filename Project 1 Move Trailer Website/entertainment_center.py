import media
"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
# movie_title, movie_story, poster_img, trailer_youtube
pk = media.Movie("PK",
                 "PK Filme",
                 "https://goo.gl/oQtbTH",
                 "https://www.youtube.com/watch?v=SOXWc32k4zA")
avatar = media.Movie("Avatar",
                     "Avatar is filem ",
                     "https://goo.gl/jtkAzH",
                     "https://www.youtube.com/watch?v=lXdgqn3p4_g")
idiots3 = media.Movie("3 Idiots",
                      "3 Idiots is A fantastic Film",
                      "https://goo.gl/K2XVF7",
                      "https://www.youtube.com/watch?v=xvszmNXdM4w")
# movies is Array conten our filmes
movies = [pk, avatar, idiots3]
# fresh_tomatoes page content html and css to show in Browser
fresh_tomatoes.open_movies_page(movies)

