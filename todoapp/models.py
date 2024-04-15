from django.db import models

# Create your models here.
class Task(models.Model):
    mailid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duetime = models.DateTimeField()
    status = models.TextField(max_length=20,default="p")

    def __str__(self):
        return self.name
    
