from django.db import models

# Create your models here.
class menu(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    mene = models.CharField(max_length=20)
    bread = models.CharField(max_length=20)
    vegetable = models.CharField(max_length=50)
    source = models.CharField(max_length=20)
    drink = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} {self.address}'