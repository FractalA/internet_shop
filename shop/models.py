from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/shop')
    category = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name
