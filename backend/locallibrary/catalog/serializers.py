from rest_framework import serializers
from .models import Author, Book, Genre, BookInstance


class LibraryStatsSerializer(serializers.Serializer):
    num_books = serializers.IntegerField()
    num_instances = serializers.IntegerField()
    num_instances_available = serializers.IntegerField()
    num_authors = serializers.IntegerField()
    num_visits = serializers.IntegerField()

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    genre = GenreSerializer(many=True)
    language = serializers.StringRelatedField()
    instance = BookInstanceSerializer(source='bookinstance_set', many=True, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

class AuthorDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(source='book_set', many=True)

    class Meta:
        model = Author
        fields = '__all__'