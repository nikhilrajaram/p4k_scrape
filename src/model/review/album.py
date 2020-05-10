class Album:
    def __init__(self, artists=[], display_name="", labels=[], photos=None, release_year=None):
        self.artists = artists
        self.display_name = display_name
        self.labels = labels
        self.photos = photos
        self.release_year = release_year
