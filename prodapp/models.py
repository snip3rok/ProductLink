from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=2, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ProductLink(models.Model):
    link = models.URLField(max_length=255)
    source = models.ForeignKey(to=Source, on_delete=models.CASCADE)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.link