# Create
from bookshelf.models import Book

Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

<!-- Expected Output: <Book: Book object (2)> -->

# Retrieve
from bookshelf.models import Book

book = Book.objects.get(id=2)
<!-- Expected Output: <Book: Book object (2)> -->

book.__dict__
<!-- Expected Output:
{'_state': <django.db.models.base.ModelState at 0x7f11f1385b50>,
 'id': 2,
 'title': '1984',
 'author': 'George Orwell',
 'publication_year': 1949}
-->

# Update
from bookshelf.models import Book

book = Book.objects.get(id=2)
book.title = "Nineteen Eighty-Four"
book.save()

<!-- Expected Output:
{'_state': <django.db.models.base.ModelState at 0x7f11f3bc3df0>,
 'id': 2,
 'title': 'Nineteen Eighty-Four',
 'author': 'George Orwell',
 'publication_year': 1949}
-->

# Delete
from bookshelf.models import Book

book = Book.objects.get(id=2)

book.delete()

Book.objects.filter(id=2).exists()


<!--Expected Output: False -->