from django.db import models

class Book(models.Model):
    book_file = models.FileField(upload_to='files/', blank=True, null=True)
    pages = models.JSONField() 
