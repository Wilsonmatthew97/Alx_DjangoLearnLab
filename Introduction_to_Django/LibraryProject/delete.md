from bookshelf.models import Book

book = Book.objects.get(title = "Nineteeen Eighty-Four")
book.delete()
# book deleted 

books = Book.objects.all()
# No books avaialable
