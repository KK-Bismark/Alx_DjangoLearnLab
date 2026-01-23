from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_date = request.POST.get("published_date")

        Book.objects.create(
                title=title,
                author=author,
                published_date=published_date,
        )
        return redirect("list_book")

    return render(request, "relationship_app/add_book.html")

@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request):
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_date = request.POST.get("published_date")
        book.save()
        
        return redirect("list_book")

    return render(request, "relationship_app/edit_book.html", {"book": book})


@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()

        return redirect("list_book")

    return render(request, "relationship_app/delete_book.html", {"book": book})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def list_books(request):
    """ Function-based view to list all books. """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """ Class-based view o display specific library and all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context = 'library'

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
