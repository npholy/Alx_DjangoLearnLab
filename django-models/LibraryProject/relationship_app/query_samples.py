from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Author Name"
books_by_author = Book.objects.filter(author__name=author_name)
print(books_by_author)

# 2. List all books in a specific library
library_name = "Library Name"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(books_in_library)

# 3. Retrieve the librarian for a library
library_name = "Library Name"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(librarian)
