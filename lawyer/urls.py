from django.urls import path
from .views import search_lawyers

urlpatterns = [
    path('search/', search_lawyers, name='search_lawyers'),
    # Add other URL patterns as needed
]


