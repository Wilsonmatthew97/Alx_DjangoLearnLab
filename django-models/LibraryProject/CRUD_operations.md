from bookshelf.models import Book

book1 = Book.objects.create(
    title = "1984",
    author = "George Orwell",
    publication_date = 1949
)
book1.save()
books = Book.objects.all()
print(books)

book = Book.objects.get(title = "1984")
print (book.title, book.author, book.publication_year)

book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id = book.id).title)

book.delete()
print(Book.objects.all())

