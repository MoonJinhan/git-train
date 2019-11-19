from django.db import models

# Create your models here.
class Question(models.Model):

    question =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DurationField(auto_now=True)

    def __str__(self):
        return self.question

    
class choice(models.Model):
    survey = models.CharField(max_length=100)
    question=models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DurationField(auto_now=True)
    votes = models.IntegerField(default=0)

      def __str__(self):
        return self.choice
