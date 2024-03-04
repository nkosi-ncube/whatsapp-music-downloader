from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    image =  image = models.ImageField(upload_to='songs', default="")

    def __str__(self):
        return self.name