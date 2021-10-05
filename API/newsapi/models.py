from django.db import models
# Create your models here.
class NewsApi(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField('images/')
    description = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self) :
        return self.title
