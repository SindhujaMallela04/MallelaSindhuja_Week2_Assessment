class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def display(self):
        print(f"{self.title} by {self.author}")
    
def main():
    book1 = Book("Six of Crows", "Leigh Bardugo", 300)
    book2 = Book("Crooked Kingdom", "Leigh Bardugo", 400)
    print(f"Total pages in the series: {book1 + book2}")
    print(f"Books in the series: ")
    book1.display()
    book2.display()
main()