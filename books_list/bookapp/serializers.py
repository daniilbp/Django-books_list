from rest_framework import serializers
from .models import Book, Profile


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name', 'title', 'author', 'description', 'price']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'column_name', 'is_visible']
