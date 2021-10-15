from django.db import models
from django.contrib.auth.models import User


def user_avatar_path(instance, filename):
    return f'user_{instance.user.id}/avatar/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    about = models.TextField(blank=True, max_length=700)
    avatar = models.ImageField(upload_to=user_avatar_path)
    
    def __str__(self):
        return self.user.username

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Advert(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField(max_length=700)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title, self.author