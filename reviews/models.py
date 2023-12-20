from django.db import models
from books.models import Book
from users.models import User
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    comment = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.comment