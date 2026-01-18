import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian



def query_books_by_author(author_name):
    """ Query all books by a specific author."""

    author = Author.objects.get(name=author_name)
    books = author.books.all()
    
    for book in books:
        print(f"{book.title}")


def list_all_books(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()

    for book in books:
        print("f{book.title")
