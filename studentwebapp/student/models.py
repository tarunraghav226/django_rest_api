from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=10)
    school_name = models.CharField(max_length=10)
    mother = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media', null=True)
    def __str__(self):
        return self.name