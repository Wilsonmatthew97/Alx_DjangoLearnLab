from bookshelf.models import Book

book = Book.objects.create(
    title = "1984",
    author = "George Orwell",
    publication_date = 1949
)

# book created successfully