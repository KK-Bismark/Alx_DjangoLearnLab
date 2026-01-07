from bookshelf.models import Book

book = Book.objects.get(id=2)
// <Book: Book object (2)>

book.__dict__
//{'_state': <django.db.models.base.ModelState at 0x7f11f1385b50>,
 'id': 2,
 'title': '1984',
 'author': 'George Orwell',
 'publication_year': 1949}