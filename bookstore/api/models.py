from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class BookStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_store = models.ForeignKey(
        BookStore, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=255, null=False, blank=False)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    descriptions = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.title
