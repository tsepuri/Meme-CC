from ..util import reddit, storage, settings, twitter
from .models import UniqueMeme
from .queries import SocialMedia
import hashlib
import time
import mimetypes

def isImage(url):
    mimetypes.init()
    mimestart = mimetypes.guess_type(url)[0]
    if mimestart != None:
        mimestart = mimestart.split('/')[0]
        return 'image' in mimestart

def load_init(limit = 100, time_filter ='day', media=['reddit','twitter']):
    kwargs = {'limit': limit/len(media), 'time_filter':time_filter} 
    if "twitter" in media:
        add_twitter_images(kwargs)
    if "reddit" in media:
        add_reddit_images(kwargs)

def add_twitter_images(kwargs):
    posts = twitter.find_images(**kwargs)
    for post_dict in posts:
        store_image(post_dict)

def add_reddit_images(kwargs):
    posts = reddit.find_images(**kwargs)
    for submission in posts:
        submission_dict = reddit.to_dict(submission)
        store_image(submission_dict)

def store_image(submission):
    query = SocialMedia()
    submission = to_dict(submission, extension = settings.DEFAULT_EXT)
    # Need to implement videos too soon
    if not query.getPost(submission['post_id']) and isImage(submission['url']):
        query.add(UniqueMeme(**submission))
        storage.storeImage(submission['url'], submission['file_name'])
def load_serve(time_interval_mins = 60, max_count = 50, limit = 10):
    count = 0
    try:
        while count < max_count:
            load_init(limit, 'hour')
            count+=limit
            time.sleep(time_interval_mins*60)
    except:
        pass
            
def to_dict(social_media_post_dictionary, extension) -> dict:

    social_media_post_dictionary.update(
        {'file_name': social_media_post_dictionary['author'][0:3]+(social_media_post_dictionary['source']).lower() + (social_media_post_dictionary.get('post_id'))[0:5]+extension}
    )
    return social_media_post_dictionary



