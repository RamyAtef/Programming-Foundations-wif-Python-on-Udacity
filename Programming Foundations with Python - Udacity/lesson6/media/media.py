import webbrowser
class Movie():

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#When Remove self From any variable this variable convert into local variable can't access it from any exist file

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        #webbrowser.open(self.poster_image_url)
