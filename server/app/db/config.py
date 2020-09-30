from .models import metadata, RedditMeme, RedditMemeTable
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os
load_dotenv()
mapper(RedditMeme, RedditMemeTable)
ENGINE = create_engine(f"postgresql+psycopg2://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DBNAME')}")
metadata.create_all(ENGINE)
CONNECTION = ENGINE.connect()
SESSION = sessionmaker(bind = ENGINE)()
METADATA = metadata