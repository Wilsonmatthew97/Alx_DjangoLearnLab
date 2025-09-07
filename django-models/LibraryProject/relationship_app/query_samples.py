from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name = 'Chinua Achebe')
books_by_author = Book.objects.filter(author = author)
for book in books_by_author:
    return f"Books by {author.name} - \n {book.title}"

library = Library.objects.get(name = "Central Library")
for book in library.books.all():
    return f"Books in {library.name} - \n {book.title}"

librarian = library.librarian
print(f"Librarian for {library.name} - {librarian.name}")
