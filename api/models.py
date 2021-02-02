from django.db import models

# Create your models here.
class Task(models.Model):
    userId=models.IntegerField()
    title=models.CharField( max_length=50)
    body=models.CharField( max_length=50)
    def __str__(self):
        return self.name