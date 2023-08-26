from mylib.LibraryProject import *

print("""

Welcome to Library Project

Transactions :

1-Show Books
2-Book Inquiry
3-Add a Book
4-Delete a Book
5-Increase Printing

If you want to exit press 'q'
*****************************
""")

lb = Library()

while True :

    process = input("Enter Your Operation : ")

    if (process == "q") :

        print("The System is Shutting Down.")
        break

    elif (process == "1") :

        lb.showBooks()

    elif (process == "2") :

        name = input("Which One You Want to Query? :")
        print("Looking...")
        time.sleep(2)

        lb.inquireBook(name)

    elif (process == "3") :

        name = input("Enter the Name of Book :")
        author = input("Enter the Author of Book :")
        publisher = input("Enter the Publisher of Book :")
        type = input("Enter the Type of Book :")
        printing = int(input("Enter the Printing of Book :"))

        newBook = Book(name,author,publisher,type,printing)

        print("The Book is Adding...")
        time.sleep(2)   
        lb.addBook(newBook)
        print("The book has been added.")

    elif (process == "4") :

        name = input("Enter the Name of Book which You Want to Delete :")

        lb.delBook(name)

        print("The book has been deleted.")

    elif (process == "5") :

        name = input("Enter the Name of Book which You Want to Increase Printing :")

        lb.increasePrinting(name)

        print("The process has been completed.")





