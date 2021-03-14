from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField()
    def __str__(self):
        return self.title
