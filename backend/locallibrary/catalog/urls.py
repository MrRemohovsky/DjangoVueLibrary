from django.urls import path

from . import views
from .views import LibraryStatsView

urlpatterns = [
    path('', views.test),
    path('api/library-stats/', LibraryStatsView.as_view(), name='library-stats'),
    path('api/book-list/', views.BookListView.as_view(), name='book-list'),
    path('api/author-list/', views.AuthorListView.as_view(), name='author-list'),
    path('api/book-detail/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('api/author-detail/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]