from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/shop')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
