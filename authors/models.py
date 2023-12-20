from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField( max_length=100)
    born_in = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name