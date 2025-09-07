from relationship_app.models import Author, Book, Library, Librarian

author_name = "Chinua Achebe"
library_name = "Central Library"

author = Author.objects.get(name = author_name)
books_by_author = Book.objects.filter(author = author)
for book in books_by_author:
    return f"Books by {author.name} - \n {book.title}"

library = Library.objects.get(name = library_name)
for book in library.books.all():
    return f"Books in {library.name} - \n {book.title}"

librarian = library.librarian
print(f"Librarian for {library.name} - {librarian.name}")
