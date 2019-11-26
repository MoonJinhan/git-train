from django.db import models

# Create your models here.
class Board(models.Model):
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)