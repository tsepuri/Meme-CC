import tweepy
from .settings import DEFAULT_LIKERS, DEFAULT_LIMIT
from dotenv import load_dotenv
import os
load_dotenv()
from datetime import datetime
def twitter_config():
    auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_KEY_SECRET'))
    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    api = tweepy.API(auth, wait_on_rate_limit=True)  
    return api
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            raise RuntimeError
def find_images(**new_settings):
    twitter = twitter_config()
    likers = new_settings.get('likers', DEFAULT_LIKERS)
    limit = new_settings.get('limit', DEFAULT_LIMIT)
    individual_limit = 10
    if limit > len(likers) * 2:
        individual_limit = 20
    tweets = []
    for liker in likers:
        tweets = tweets + (get_tweets_from_favorites(liker,twitter, individual_limit, tweets))
        if len(tweets) >= limit:
            break
    return tweets
def get_tweets_from_favorites(liker, api, limit, tweets):
    selected_tweets = []
    for tweet in limit_handled(tweepy.Cursor(api.favorites, id=liker).items(limit)):
        username = tweet.user.screen_name
        favorites = tweet.favorite_count
        retweets = tweet.retweet_count
        # Removing URL at end of all tweets
        text = tweet.text[0:tweet.text.find("https://t.co")]
        postid = tweet.id
        post_ids = [tweet['post_id'] for tweet in tweets]
        if postid in post_ids:
            continue
        url = f"https://www.twitter.com/{username}/status/{postid}"
        media_url = look_for_media(tweet)
        if media_url == "NOT_CHOSEN":
            continue
        if tweet.is_quote_status and hasattr(tweet, 'quoted_status'):
            new_media_url = look_for_media(tweet.quoted_status)
            if new_media_url != "NOT_CHOSEN" and new_media_url != "":
                media_url = new_media_url
            text = text + f"\nRetweet of: {tweet.quoted_status.text} by {tweet.quoted_status.user.screen_name}"
        # Conditions that usually result in memes based on experience
        if favorites < (retweets * 12) and favorites > 10000 and not tweet.user.verified and not tweet.truncated:
            if media_url == "":
                media_url = "https://dummyimage.com/400x400/ffffff/000000&text=No+image"
            selected_tweets.append(to_dict(tweet, media_url, url, text))
    return selected_tweets
def to_dict(submission, media_url, url, text):
    return {'post_id':str(submission.id), 
            'likes':submission.favorite_count, 
            'url' : media_url,
            'shortlink':url,
            'author':submission.user.screen_name,
            'title': text,
            'created_at':submission.created_at,
            'source': "Twitter"
            }
def look_for_media(tweet):
    if 'media' in tweet.entities:
        images = len(tweet.entities["media"])
        if images > 1:
            return "NOT_CHOSEN"
        image_url = tweet.entities["media"][0]["media_url"]
        return look_for_video(tweet, image_url)     
    return ""
def look_for_video(tweet, image_url):
    if "video_thumb" in image_url:
        try:
            image_url = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
        except Exception:
            pass
        if "mp4" not in image_url:
            try:
                image_url = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
            except Exception:
                pass
            # Sometimes Twitter doesn't allow you to access the video file, in which case it's ignored
            if "mp4" not in image_url:
                return "NOT_CHOSEN"
    return image_url

'''
trends_result = api.trends_place(23424977)
for trend in trends_result[0]["trends"]:
    print(trend["name"])
'''
