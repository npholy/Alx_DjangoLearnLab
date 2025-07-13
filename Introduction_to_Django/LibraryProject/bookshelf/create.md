# Create Operation 
```python 
from bookshelf.models import Book 
book = Book(title="1984", author="George Orwell", publication_year=1949) 
book.save() 
``` 
*Expected Output*: No output on successful save; the book is created in the database. 
