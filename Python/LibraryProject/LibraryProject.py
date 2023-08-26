import time
import sqlite3

class Book () :

    def __init__(self,name,author,publisher,type,printing) :

        self.name = name
        self.author = author
        self.publisher = publisher
        self.type = type
        self.printing = printing

    def __str__(self) :

        return "Book : {}\nAuthor : {}\nPublisher : {}\nType : {}\nPrinting : {}\n".format(self.name,self.author,self.publisher,self.type,self.printing)



class Library () :

    def __init__(self) :
        self.connect()

    def connect (self) :

        self.connection = sqlite3.connect("library.db")

        self.cursor = self.connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS Books (Name TEXT,Author TEXT,Publisher TEXT,Type TEXT,Printing INT)"

        self.cursor.execute(query)

        self.connection.commit()

    def disConnect (self) :

        self.connection.close

    def showBooks (self) :

        query = "Select * From Books"

        self.cursor.execute(query)
        Books  = self.cursor.fetchall()

        if (len(Books) == 0) :

            print("There is no book in library")

        else :

            for i in Books :

                book = Book(i[0],i[1],i[2],i[3],i[4])

                print(book)

    def inquireBook (self,name) :

        query = "Select * From Books where Name = ?"
        self.cursor.execute(query,(name,))

        Books  = self.cursor.fetchall()

        if (len(Books) == 0) :

            print("This book doesnt exist in library.")

        else :

            book = Book(Books[0][0],Books[0][1],Books[0][2],Books[0][3],Books[0][4])

            print(book)

    def addBook (self,book) :

        query = "Insert into Books Values(?,?,?,?,?)"

        self.cursor.execute(query,(book.name,book.author,book.publisher,book.type,book.printing))

        self.connection.commit()

    def delBook (self,name) :

        query = "Delete From Books where Name = ?"

        self.cursor.execute(query,(name,))

        self.connection.commit()

    def increasePrinting (self,name) :

        query = "Select * From Books where Name = ?"

        self.cursor.execute(query,(name,))

        books = self.cursor.fetchall()

        if (len(books) == 0) :

            print("This book doesnt exist in library.")

        else :

            printing = books[0][4]

            printing += 1

            query2 = "Update Books set printing = ? where Name = ?"

            self.cursor.execute(query2,(printing,name,))

        self.connection.commit()






