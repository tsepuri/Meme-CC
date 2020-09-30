from . import models, queries
from datetime import datetime
redditMeme = models.RedditMeme("AXHNN0", 56, "bing.com", "ddd", "John Doe", title="Good shoes", created_at=datetime.utcnow(), file_name="axb5", source="Twitter")
redditdb = queries.Reddit()
#redditdb.add(redditMeme)
print(redditdb.getRandom())