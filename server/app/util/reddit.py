import praw
from dotenv import load_dotenv
import os
import sys
from . import settings
from datetime import datetime
load_dotenv()
def reddit_config():
    reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     user_agent="MemeCC 1.0")
    return reddit

def find_images(**new_settings) -> dict:
    reddit = reddit_config() 
    time_filter = new_settings.get('time_filter', settings.TIME_FILTER)
    subreddits = new_settings.get('subreddits', settings.DEFAULT_SUBREDDITS)
    limit = new_settings.get('limit', settings.DEFAULT_LIMIT)
    return reddit.subreddit(subreddits).top(time_filter=time_filter,limit = limit)  
def to_dict(submission):
    return {'post_id':submission.id, 
            'likes':submission.score, 
            'url' :submission.url,
            'shortlink':submission.shortlink,
            'author':submission.author.name,
            'title':submission.title,
            'created_at':datetime.utcfromtimestamp(submission.created_utc),
            'source': "Reddit"
            }
 
