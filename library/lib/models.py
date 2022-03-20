from django.db import models

class Book(models.Model):
    book_file = models.FileField(upload_to='files/', blank=True, null=True) 

class PageOfBook(models.Model):
    page_file = models.FileField(upload_to='pages/', blank=True, null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)



