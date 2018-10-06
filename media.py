import webbrowser


class Movie():
    """
    This class provides a way to store movie related information

	Attributes:
	title(str): describes movie title.
	storyline(str): describes story of movie
	poster_image(str): has poster image link for the movie
	trailer_youtube(str): has youtube trailer link for the movie
    """

    # Constructer get's initialise when instances are created.
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        # Instance variables store data of class Movie
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open youtube trailer in Webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
