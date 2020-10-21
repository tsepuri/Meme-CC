from . import models, queries
from datetime import datetime
uniqueMeme = models.UniqueMeme("AXHNN0", 56, "bing.com", "ddd", "John Doe", title="Good shoes", created_at=datetime.utcnow(), file_name="axb5", source="Twitter")
socialmediadb = queries.SocialMedia()
socialmediadb.add(uniqueMeme)
print(socialmediadb.getRandom())