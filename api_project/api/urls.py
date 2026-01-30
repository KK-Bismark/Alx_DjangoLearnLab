from .views import BookList
from django.urls import path


urlpatterns = [
   path('books/', BookList.as_view(), name='book-list'), # Maps to BookList view
]
