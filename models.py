from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create db
engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base

Session = engine
session = session()

def_tablename == 'books'

# books.db
# create a model
# title, author, date published, price
