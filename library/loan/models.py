from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    # age = models.PositiveIntegerField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=50, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
                # blank=True means field is NOT REQUIRED
    def __str__(self):
        return f'{self.title} ({self.author.name})'