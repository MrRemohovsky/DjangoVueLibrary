from rest_framework import serializers
from .models import Author, Book, Genre


class LibraryStatsSerializer(serializers.Serializer):
    num_books = serializers.IntegerField()
    num_instances = serializers.IntegerField()
    num_instances_available = serializers.IntegerField()
    num_authors = serializers.IntegerField()
    num_visits = serializers.IntegerField()

class AuthorSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = '__all__'
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    genre = GenreSerializer(many=True)
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()
