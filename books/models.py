from django.db import models
from authors.models import Author
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    
    def __str__(self) -> str:
        return self.title