import webbrowser


class Movie():
    """This defines an instance of a movie including a description of the
        storyline, poster image, trailer url."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Constructor to initialize title, storyline, poster image and
            trailer url"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Function that opens the trailer url in a browser window"""
        webbrowser.open(self.trailer_youtube_url)
