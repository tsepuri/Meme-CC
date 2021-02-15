from .config import SESSION, ENGINE, METADATA
from .models import UniqueMeme, Template
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
        self.table.drop(ENGINE)
    def getPost(self, postID):
        return SESSION.query(UniqueMeme).filter_by(post_id = postID).first()
    # Need to add search feature after tesseract and neural net
# Might make a new table and class for the examples of the templates, since the name is confusing and 
# will make it easier to search with JOIN
class Templates():
    table = []
    def __init__(self):
        self.table = METADATA.tables['meme_templates']
    def add(self, template):
        SESSION.add(template)
        SESSION.commit()
    def dropTable(self):
        self.table.drop(ENGINE)
    def getBySearch(self, searched, **extra_filters):
        # Will need to filter text too, once tesseract is built in
        query = SESSION.query(Template).filter(Template.description.ilike(f'%{searched}%') | Template.title.ilike(f'%{searched}%'))
        for extra_filter in extra_filters:
            query = query.filter(getattr(Template, extra_filter) == extra_filters[extra_filter])
        return query.all()
    def getAll(self, templates_only=False):
        return SESSION.query(Template).filter(Template.template == templates_only).all()
# change to mixin
def getByFile(filename):
    return SESSION.query(Template).filter(Template.file_name == filename).first() or SESSION.query(UniqueMeme).filter(UniqueMeme.file_name == filename).first()
def getBySearch(searched):
    return SESSION.query(UniqueMeme).filter(similarSearchTerm(UniqueMeme.title, searched) | similarSearchTerm(UniqueMeme.text, searched)).all() 
    + SESSION.query(Template).filter(similarSearchTerm(Template.description, searched) | similarSearchTerm(Template.title, searched) | similarSearchTerm(Template.text, searched)).all()
    
def similarSearchTerm(db_column, searchTerm):
    return db_column.ilike(f'%{searchTerm}%')
    