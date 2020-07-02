from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Student(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    school_name = models.CharField(max_length=10)
    mother = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media', null=True)
    
    def __str__(self):
        return self.name


class Subjects(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=10)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
