from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
orwell_books = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:", list(orwell_books))

# 2. List all books in a specific library
library = Library.objects.get(name="Central Library")
print("Books in Central Library:", list(library.books.all()))

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for Central Library:", librarian.name)
