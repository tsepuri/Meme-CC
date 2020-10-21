from .queries import SocialMedia
from ..util import storage
query = SocialMedia()
try:
    query.dropTable()
except Exception:
    pass
storage.clean()
