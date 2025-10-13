from django.db import models

# Create your models here.
class Student (models.Model)
    name = models.charField(max_length=50)
    age = models.IntegerField(default=18)
    hometown = models.TextField(max_length=50)
    email = models.EmailField()
    poitrait = models.ImageField()
    file = models.FileField()
