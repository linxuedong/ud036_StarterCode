class Movie():
    """Data structure to store movie.

    Attributes:
        title(str): The name of movie
        story_line(str): The story line of movie
        poster_image_url(str): The cover of movie
        trailer_youtube_url(str): The link of this movie's trailer
    """

    def __init__(self, title, story_line, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
