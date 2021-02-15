from sqlalchemy import Column, Integer, String, DateTime, Table, select, MetaData, Boolean
import sqlalchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass, field
Base = declarative_base()
metadata = MetaData()
TemplatesTable = \
    Table('meme_templates', metadata,
          Column('_id', Integer, primary_key=True),
          Column('likes', Integer),
          Column('template', Boolean),
          Column('url', String(200)),
          Column('shortlink', String(300)),
          Column('title', String(1000), nullable=False),
          Column('description', String(1000)),
          Column('file_name', String(100)),
          Column('source', String(10)),
          Column('text', String(300))
          )
UniqueMemeTable = \
    Table('unique_memes', metadata,
          Column('_id', Integer, primary_key=True),
          Column('post_id', String(100)),
          Column('likes', Integer),
          Column('url', String(200)),
          Column('shortlink', String(300)),
          Column('author', String(100)),
          Column('created_at', DateTime),
          Column('title', String(1000), nullable=False),
          Column('file_name', String(100)),
          Column('source', String(10)),
          Column('text', String(300))
          )
@dataclass
class UniqueMeme:
    post_id: str 
    likes: int
    url: str 
    shortlink: str 
    author: str 
    title: str 
    created_at: datetime
    file_name: str
    source: str
    text: str

@dataclass
class Template:
    likes: int
    template: bool
    url: str 
    shortlink: str
    title: str
    description: str 
    file_name: str 
    source: str
    text: str
    