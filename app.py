from models import (Base, session, Book, engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
# main menu - add, search, analysis, exit, view
# add books to the database
# edit
# delete
# search
# data cleaning
# loop runs program
