from .config import SESSION, ENGINE, METADATA
from .models import RedditMeme
from sqlalchemy.sql.expression import func, select
class Reddit():
    table = []
    def __init__(self):
        self.table = METADATA.tables['reddit_memes']
    def getRandom(self, limit=1) -> RedditMeme:
        return SESSION.query(RedditMeme).order_by(func.random())[:limit]
    def add(self, redditMeme):
        SESSION.add(redditMeme)
        SESSION.commit()
    def delete(self, postID):     
        ENGINE.execute(self.table.delete().where(self.table.c.post_id == postID))
    def dropTable(self):
        ENGINE.execute(self.table.drop(ENGINE))
    def getPost(self, postID):
        return SESSION.query(RedditMeme).filter_by(post_id = postID).first()
    def getFile(self, filename):
        return SESSION.query(RedditMeme).filter_by(file_name = filename).first()

    