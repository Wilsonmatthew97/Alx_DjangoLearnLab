from bookshelf.models import Book

book = Book.objects.get(title = "1984")

print("Title:", book.title)
 # "1984"
print("Author:", book.author)
 # "George Orwell"
print("Publication_date:", book.publication_date)
 # 1949
