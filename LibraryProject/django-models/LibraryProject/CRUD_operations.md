# CRUD Operations 
## Create 
```python 
from bookshelf.models import Book 
book = Book(title="1984", author="George Orwell", publication_year=1949) 
book.save() 
``` 
*Expected Output*: No output on successful save; the book is created in the database. 
 
## Retrieve 
```python 
from bookshelf.models import Book 
book = Book.objects.get(title="1984") 
print(book.id, book.title, book.author, book.publication_year) 
``` 
*Expected Output*: `1 1984 George Orwell 1949` 
 
## Update 
```python 
from bookshelf.models import Book 
book = Book.objects.get(title="1984") 
book.title = "Nineteen Eighty-Four" 
book.save() 
print(book.title) 
``` 
*Expected Output*: `Nineteen Eighty-Four` 
 
## Delete 
```python 
from bookshelf.models import Book 
book = Book.objects.get(title="Nineteen Eighty-Four") 
book.delete() 
print(Book.objects.all()) 
``` 
