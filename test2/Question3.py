class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_book_details(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"ISBN: {self.__isbn}")

def get_input():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    isbn = input("Enter the book ISBN: ")
    print()
    return title, author, isbn

def main():
    print("Welcome to the Library")
    books = []
    while(1): 
        print()       
        print("1. Add a book")
        print("2. See the book catalog")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            book = Book(title, author, isbn)
            #Logic for Checking if the book already exists in the catalog
            flag = 0
            for book in books:
                if book._Book__isbn == isbn:
                    flag = 1
                    break
            if flag == 1:
                    print(f"The book \"{title}\" already exists in the catalog. Check the ISBN if it is a different book.")
            else:            
                print()
                print(f"Book {title} has been added to the catalog.")
                books.append(book)

        elif choice == 2:
            print()
            if books == []:
                print("No books in the catalog. Add books to see the catalog.")
            else:
                print("The books in the Library are: ")
                for book in books:
                    book.get_book_details()

        elif choice == 3:
            break
        else:
            print("Invalid Choice. Please try again.")

main()