#Configuration file for the server -> APIs, databases URIs ...
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv() #loads the vairbales in .env into memory 


"""Configuring the server's databases"""
#relational -> Postgres 
class Base(DeclarativeBase):
    pass

POSTGRES_URI = os.getenv('POSTGRES_URI')
if not POSTGRES_URI:
    raise ValueError('Unable to retrieve the Postgres URI from the .env file.')