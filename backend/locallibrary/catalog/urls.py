from django.urls import path

from . import views
from .views import LibraryStatsView

urlpatterns = [
    path('', views.test),
    path('api/library-stats/', LibraryStatsView.as_view(), name='library-stats'),
]