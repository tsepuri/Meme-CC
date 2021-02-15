from .queries import SocialMedia, Templates
from ..util import storage
def dropTable(query):
    try:
        query.dropTable()
    except Exception:
        pass
dropTable(SocialMedia())
dropTable(Templates())
storage.clean()
