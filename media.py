import webbrowser

""" Anime class that contains all information of anime
"""
class Anime():
    """ Initializer function
        params:
            title: Anime title
            storyline: Anime storyline
            poster_image_url: Url of the anime poster
            trailer_youtube_url: Url of a youtube url
    """
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    """ Function: Show trailer
        Uses webbrowser to open the trailer_youtube_url property of the class
    """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
