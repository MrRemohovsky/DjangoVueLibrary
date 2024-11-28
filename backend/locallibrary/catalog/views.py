from django.core.cache import cache
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, BookInstance, Author
from .serializers import LibraryStatsSerializer, BookSerializer, AuthorSerializer, AuthorDetailSerializer


def test(request):
    return render(request, 'catalog/test.html')

class LibraryStatsView(APIView):
    def get(self, request, *args, **kwargs):
        cache_key = 'library_stats'
        cache_data = cache.get(cache_key)

        if cache_data:
            return Response(cache_data)

        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()
        num_instances_available = BookInstance.objects.filter(status__exact='a').count()
        num_authors = Author.objects.count()

        if not request.session.session_key:
            request.session.create()

        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1

        data = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_visits': request.session['num_visits']
        }
        serializer = LibraryStatsSerializer(data)
        cache.set(cache_key, serializer.data, timeout=1)
        return Response(serializer.data)

class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        cache_key = 'book_list'
        cache_data = cache.get(cache_key)

        if cache_data:
            return Response(cache_data)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        cache.set(cache_key, serializer.data, timeout=300)
        return Response(serializer.data)

class AuthorListView(APIView):
    def get(self, request, *args, **kwargs):
        cache_key = 'author_list'
        cache_data = cache.get(cache_key)

        if cache_data:
            return Response(cache_data)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        cache.set(cache_key, serializer.data, timeout=300)
        return Response(serializer.data)

class BookDetailView(APIView):
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        serializer = BookSerializer(book)
        return Response(serializer.data)

class AuthorDetailView(APIView):
    def get(self, request, *args, **kwargs):
        author = Author.objects.get(pk=kwargs['pk'])
        serializer = AuthorDetailSerializer(author)
        print(serializer.data)
        return Response(serializer.data)













