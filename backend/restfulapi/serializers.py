from rest_framework import serializers
from book.models import Category, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Book
        fields = ('title', 'cover', 'description', 'douban_score', 'users', 'tags')