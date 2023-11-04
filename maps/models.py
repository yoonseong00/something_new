from django.db import models

# Create your models here.

class Kakaomap(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()