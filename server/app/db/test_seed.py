from . import models, queries
from datetime import datetime
'''
uniqueMeme = models.UniqueMeme("AXHNN0", 56, "bing.com", "ddd", "John Doe", title="Good shoes", created_at=datetime.utcnow(), file_name="axb5", source="Twitter")
'''
socialmediadb = queries.SocialMedia()
'''
socialmediadb.add(uniqueMeme)
print(socialmediadb.getRandom())
template = models.Template(9, False, "bing.com", "google.com", "Template shoes", "Lookin good", "ab5", source="KYM")
'''
templatedb = queries.Templates()
'''
templatedb.add(template)
print(templatedb.getBySearch("award", **{'template':False}))
'''
templatedb.dropTable()
socialmediadb.dropTable()