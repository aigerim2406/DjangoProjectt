from django.db import models

class Aigerim(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    price = models.BigIntegerField(default=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

def __str__(self):
    return self.name