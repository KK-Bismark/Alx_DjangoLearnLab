from bookshelf.models import Book

book = Book.objects.get(id=2)

book.delete()

Book.objects.filter(id=2).exists()

<!--Expected Output: False -->