from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    descriptions = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.title
