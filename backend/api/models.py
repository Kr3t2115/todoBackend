from statistics import mode
from django.db import models

# Create your models here.
class todoModel(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    completed = models.BooleanField()
