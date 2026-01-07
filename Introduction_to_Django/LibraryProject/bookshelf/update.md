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