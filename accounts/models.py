from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    avatar = models.ImageField()

    def __str__(self):
        return self.get_full_name()