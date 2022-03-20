from msilib.schema import File, ListView
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer, PageOfBookSerializer
from rest_framework import status

from .models import Book, PageOfBook
from lib.services.book_services import cut_on_page
from lib.services.book_services import cut_on_page_pyPDF2

class BookViev(APIView):
    def get(self, request, id=None):
        if id:
            try:
                book = Book.objects.get(id=id)
                serializer = BookSerializer(book)
                return Response(serializer.data)
            except:
                return Response(status=status.HTTP_204_NO_CONTENT)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book = Book(book_file=request.FILES['file'])
        book.save()
        pages = cut_on_page_pyPDF2(book.book_file)
        for file in pages:
           page = book.pageofbook_set.create(page_file=file)
           page.save()
        
        serializer = BookSerializer(book)
        book.save()
        return Response(serializer.data)
    
    def delete(self, request, id=None):
        if id:
            try:
                Book.objects.get(id=id).delete()
            except:
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_202_ACCEPTED)

        Book.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PageOfBookViev(APIView):
    def delete(self, request, book_id ,page_number=None):
        if id:
            try:
                book = Book.objects.get(id=book_id)
                pages = book.pageofbook_set.all()
                pages[page_number].delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except:
                return Response("Index error")
        else:
             book = Book.objects.get(id=book_id)
             book.pageofbook_set.all().delete()
             return Response(status=status.HTTP_204_NO_CONTENT)


    def get(self, request, book_id=None, page_number=None):
        book = Book.objects.get(id=book_id)
        pages = book.pageofbook_set.all()
        #serilizer = PageOfBookSerializer(pages, many=True)
        try:
            return FileResponse(pages[page_number].page_file)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
   

    
# Create your views here.
