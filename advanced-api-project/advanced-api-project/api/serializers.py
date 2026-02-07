from .models import Author, Book
from datetime import datetime
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    """ Book model serializer. """
    class meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Validates the publication year
        so as to prevent books from
        being published in the future.
        """
        current_year = datetime.now().year
        if valuse > current_year:
            raise serializers.ValidationError(
            "Publication year cannot be in the future"
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """ Author model serializer. """
    
    books = BookSerializer(many=True, read_only=True)

    class meta:
        model = Author
        fields = 'name'
