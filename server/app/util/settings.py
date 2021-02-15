import os
from dotenv import load_dotenv
load_dotenv()
#server
PORT = int(os.environ.get("PORT", 5000))

#storage
if os.getenv("LOCAL") == "true":
    if not os.path.exists(os.getenv("LOCAL_PATH")):
        raise ValueError
#reddit
# Funny subreddits on reddit
DEFAULT_SUBREDDITS = "dankmemes+memes"
DEFAULT_LIMIT =  5
DEFAULT_EXT = ".png"
TIME_FILTER = "week"

#twitter
# Accounts who like funny posts on Twitter
DEFAULT_LIKERS = ["CosmonautMarcus", "richbrian", "WhosBreezyUK", "Quackity", "Memeulous", "grandayy", "CaucasianJames", "lilsasquatch66"]
# Dummy image for posts that only have text
DUMMY_URL = "dummyimage.com/400x400/ffffff/000000&text=No+image"