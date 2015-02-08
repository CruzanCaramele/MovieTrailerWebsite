"""This is where the Movie class gets defined and the instance variables are
initialized."""


import webbrowser

class Movie():
    #constructor, creates a movie object
    def __init__(self, movie_title, movie_storyline,
                 poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    """ A function that takes in an instance of the Movie class
    and opens it's trailer in the web browser"""
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
