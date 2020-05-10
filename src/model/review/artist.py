class Artist:
    def __init__(self, display_name="", genres=[], artist_id=None, photos=None, slug=None, url=""):
        self.display_name = display_name
        self.genres = genres
        self.id = artist_id
        self.photos = photos
        self.slug = slug
        self.url = url
