class Review:
    def __init__(self, artists=[], authors=[], channel="", content_type="", dek="", genres=[], id=None,
                 modified_at=None, position=None, private_tags=[], promo_description="", promo_title="",
                 pub_date=None, seo_description="", seo_title="", social_description="", social_title="",
                 sub_channel="", tags=[], timestamp=None, title="", tombstone=None, url=""):
        self.artists = artists
        self.authors = authors
        self.channel = channel
        self.content_type = content_type
        self.dek = dek
        self.genres = genres
        self.id = id
        self.modified_at = modified_at
        self.position = position
        self.private_tags = private_tags
        self.promo_description = promo_description
        self.promo_title = promo_title
        self.pub_date = pub_date
        self.seo_description = seo_description
        self.seo_title = seo_title
        self.social_description = social_description
        self.social_title = social_title
        self.sub_channel = sub_channel
        self.tags = tags
        self.timestamp = timestamp
        self.title = title
        self.tombstone = tombstone
        self.url = url
