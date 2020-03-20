from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Categorie(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    rating = models.FloatField(default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    #asin = models.IntegerField(unique=True)
    warranty = models.BooleanField(default=True)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_comments(self):
        return Review.objects.filter(product=self)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)


class Bucket(models.Model):
    session_key = models.CharField(max_length=100)
    product = models.ManyToManyField(Product)

