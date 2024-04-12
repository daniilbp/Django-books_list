from django.urls import path

from .views import book, profile

app_name = "bookapp"

urlpatterns = [
    path('main/', book, name='books'),
    path('main/', profile, name='profiles'),
    path('main/book_<str:action>/', book, name='book_create'),
    path('main/<str:action>_book_<int:pk>/', book, name='book_action'),
    path('main/update_profiles/', profile, name='update_profiles'),
]
