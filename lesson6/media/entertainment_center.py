import media 
import fresh_tomatoes

 #(toy_story) => objct from class(Movie) 
toy_story = media.Movie("Toy Story",
                          "A Story od a boy and his toys that come to life",
                          "https://animationfascination.files.wordpress.com/2013/11/toy_story.jpg",
                          "https://www.youtube.com/watch?v=WPUJQow1QlY")
#print(toy_story.trailer_youtub_url)

avatar = media.Movie("Avatar",
                     "Avatar is filem ",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=lXdgqn3p4_g")
#print(avatar.storyline)
#avatar.show_trailer()
idiots3 = media.Movie("3 Idiots",
                      "3 Idiots is A fantastic Film",
                      "http://sites.psu.edu/pragnyaprabakaran/wp-content/uploads/sites/38771/2016/04/3i-poster-3.jpg",
                      "https://www.youtube.com/watch?v=xvszmNXdM4w")


#print(idiots3.title)
#idiots3.show_trailer()

movies = [toy_story,avatar,idiots3]
fresh_tomatoes.open_movies_page(movies)


