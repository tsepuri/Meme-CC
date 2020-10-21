from .config import SESSION, ENGINE, METADATA
from .models import UniqueMeme
from sqlalchemy.sql.expression import func, select
class SocialMedia():
    table = []
    def __init__(self):
        self.table = METADATA.tables['unique_memes']
    def getRandom(self, limit=1) -> UniqueMeme:
        return SESSION.query(UniqueMeme).order_by(func.random())[:limit]
    def add(self, uniqueMeme):
        SESSION.add(uniqueMeme)
        SESSION.commit()
    def delete(self, postID):     
        ENGINE.execute(self.table.delete().where(self.table.c.post_id == postID))
    def dropTable(self):
        ENGINE.execute(self.table.drop(ENGINE))
    def getPost(self, postID):
        return SESSION.query(UniqueMeme).filter_by(post_id = postID).first()
    def getFile(self, filename):
        return SESSION.query(UniqueMeme).filter_by(file_name = filename).first()

    