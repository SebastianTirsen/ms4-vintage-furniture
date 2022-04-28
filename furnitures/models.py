from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_fiendly_name(self):
        return self.friendly_name


class Furniture(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=254)
    material = models.CharField(max_length=254)
    production = models.CharField(max_length=254)

    choices = (
            ('Like New', 'Like New'),
            ('Good', 'Good'),
            ('Worn', 'Worn'),
        )

    condition = models.CharField(max_length=300, null=True, blank=True, choices=choices)

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Support(models.Model):
    name = models.CharField(max_length=130)
    description = models.TextField(blank=True)
