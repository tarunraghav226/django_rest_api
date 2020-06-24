from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=10)
    school_name = models.CharField(max_length=10)
    mother = models.CharField(max_length=10)

    class Meta:
        db_table = 'Student'

    def __str__(self):
        return self.name