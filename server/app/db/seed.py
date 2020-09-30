from ..util import reddit, storage, settings
from .models import RedditMeme
from .queries import Reddit
import hashlib
import time
import mimetypes

def isImage(url):
    mimetypes.init()
    mimestart = mimetypes.guess_type(url)[0]
    if mimestart != None:
        mimestart = mimestart.split('/')[0]
        return 'image' in mimestart

def load_init(limit = 100, time_filter ='day'):
    kwargs = {'limit': limit, 'time_filter':time_filter} 
    posts = reddit.find_images(**kwargs)
    redditQuery = Reddit()
    for submission in posts:
        submission = to_dict(reddit.to_dict(submission), extension = settings.DEFAULT_EXT)
        if not redditQuery.getPost(submission['post_id']) and isImage(submission['url']):
            redditQuery.add(RedditMeme(**submission))
            storage.storeImage(submission['url'], submission['file_name'])
def load_serve(time_interval_mins = 60, max_count = 50, limit = 10):
    count = 0
    kwargs = {'limit':limit, 'time_filter':'hour'}
    try:
        while count < max_count:
            load_init(limit, 'hour')
            count+=limit
            time.sleep(time_interval_mins*60)
    except:
        pass
            
def to_dict(social_media_post_dictionary, extension) -> dict:
    social_media_post_dictionary.update(
        {'file_name': social_media_post_dictionary.get('title').split()[0] + social_media_post_dictionary.get('post_id')+extension}
    )
    return social_media_post_dictionary



