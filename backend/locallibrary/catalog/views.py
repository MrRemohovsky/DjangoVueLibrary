from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, BookInstance, Author
from .serializers import LibraryStatsSerializer, BookSerializer, AuthorSerializer, AuthorDetailSerializer


def test(request):
    return render(request, 'catalog/test.html')

class LibraryStatsView(APIView):
    def get(self, request, *args, **kwargs):
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
        return Response(serializer.data)

class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class AuthorListView(APIView):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
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













