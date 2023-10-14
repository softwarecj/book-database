from models import (Base, session, Book, engine)
import datetime
import csv
import time


# main menu - add, search, analysis, exit, view
# r is caret return will print where the return is
def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1) Add book
        \r2) View all books
        \r3) Search for book
        \r4) Book Analysis
        \r5) Exit''')

        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
    
        else: 
            input('''
              Please choose one of the options above.
              A number from 1=5.
              Press enter to try again
              ''')
    
# add books to the database
# edit
# delete
# search
# data cleaning
def cleanData(dateStr):
    #can also use strptime()
    months = ['January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August', 'September',
            'October', 'November', 'December']
    #splitting the month, day, and year in a 3 split
    splitDate = dateStr.split(' ')
    try:
    #adding 1 to the index so January can start at 1 and not 0
        month = int(months.index(splitDate[0])+1)
    #splitting index 1(ex. 25, in October 25, 2017) and taking out the , after 25 which takes the first index[0] shown at the end.
        day = int(splitDate[1].split(',')[0])
        year = int(splitDate[2])
        dateReturn = datetime.date(year, month, day)
    except ValueError:
        input('''
              \n*********DATE ERROR*********
              \rThe date format should include a vaide Month Date Year format
              \rEX: January 1, 2023
              \rPress enter to try again.
              \r*****************************''')
        return None

    else:
        return dateReturn
def cleanPrice(priceStr):
    try:
        priceFloat = float(priceStr)
    except ValueError:
        input('''
              \n*********PRICE ERROR*********
              \rThe price format should be a number without a $ symbol
              \rEX: 29.99
              \rPress enter to try again.
              \r******************************''')
        return None
    #removing the decimal ex. 29.99 to 2999
    else:
        return(int(priceFloat * 100))
    
# loop runs program

def addCSV():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        #print every row in the csv file
        for row in data:
            #to keep from making duplicate books/ .one_or_none, looks for at least one or or none books
            bookIndatabase = session.query(Book).filter(Book.title == row[0]).one_or_none()
            #if books are = to none, then all of indention will be added in session
            if bookIndatabase == None:
                title = row[0]
                author = row[1]
                date = cleanData(row[2])
                price = cleanPrice(row[3])
                newBook = Book(title = title, author = author, published_date = date, price = price)
                session.add(newBook)
            session.commit()



def app():
    runningApp = True
    while runningApp:
         choice = menu()
         if choice == '1':
            title = input('Title: ')
            author = input('Author: ')
            dateError = True
            while dateError:
                date = input('Published Date (In format October 25, 2020): ')
                date = cleanData(date)
                if type(date) == datetime.date:
                    dateError = False
            priceError = True
            while priceError:
                price = input('Price of book: (In format XX.xx)')
                price = cleanPrice(price)
                if type(price) == int:
                    priceError = False
            newBook = Book(title = title, author = author, published_date = date, price = price)
            session.add(newBook)
            session.commit()
            print(f'**{newBook.title}** was added!')
            #Will pause for 1.5 seconds before continuing on
            time.sleep(1.5)
         elif choice == '2':
             pass
         elif choice == '3':
             pass
         elif choice == '4':
             pass
         else:
             print('Good Bye!')
             runningApp = False
        
        


            


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    #menu()
    # Don't need to run menu anymore, just run app()
    #app()
    #addCSV()
    addCSV()
    app()

    for book in session.query(Book.title, Book.author, Book.published_date, Book.price):
        print(book)

