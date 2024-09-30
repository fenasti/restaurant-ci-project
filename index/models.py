from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)


# featured_image = CloudinaryField('image', default='placeholder')