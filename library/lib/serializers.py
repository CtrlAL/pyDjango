from importlib.metadata import requires
from tkinter import PAGES
from rest_framework import serializers
from .models import Book, PageOfBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','book_file')


class PageOfBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageOfBook
        fields = ('id','page_file')