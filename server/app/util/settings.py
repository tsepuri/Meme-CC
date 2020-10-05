import os
from dotenv import load_dotenv
load_dotenv()
#server
PORT = int(os.environ.get("PORT", 5000))

#storage
if os.getenv("LOCAL"):
    if not os.path.exists(os.getenv("LOCAL_PATH")):
        raise ValueError
#reddit
DEFAULT_SUBREDDITS = "dankmemes+memes"
DEFAULT_LIMIT = 1
DEFAULT_EXT = ".png"
TIME_FILTER = "week"