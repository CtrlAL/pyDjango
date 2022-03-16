from urllib import request
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework import status

from .models import Book
from lib.services.book_services import cut_on_page

class BookViev(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self,request):
        p = cut_on_page(request.FILES['file'])
        book = Book(book_file=request.FILES['file'], pages=p)
        dna = BookSerializer(book, data=request.data)
        print(dna.initial_data)
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data)

# def get_pages(request, id):
#     book = Book.objects.get(book_id=id)
#     return book

# Create your views here.
