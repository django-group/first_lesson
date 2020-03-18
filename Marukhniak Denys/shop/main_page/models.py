from django.db import models
from django.template.defaultfilters import slugify


# Что бы можно было для одного продукта группировать фото по папкам.

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/slug>/<filename>
#     return '{0}/{1}'.format(instance.slug, filename)

# image = models.ImageField(upload_to=user_directory_path)


class Specification(models.Model):
    name = models.CharField(max_length=30)
    text_spec = models.CharField(max_length=75)

    def __str__(self):
        return str(self.name) + ': ' + str(self.text_spec)


class Product(models.Model):
    specifications = models.ManyToManyField(Specification)
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=75)
    #  height_field=256, width_field=256
    image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.PositiveIntegerField()
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    amount_of_review = models.PositiveIntegerField(default=0)
    discount = models.IntegerField(default=0)
    product_code = models.IntegerField()
    guarantee = models.BooleanField()
    # author = models.CharField(max_length=40)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_rating(self):
        ratings = Review.objects.filter(product=self)
        ratings_int = [item.rating_rev for item in ratings]
        ratings_sum = sum(ratings_int)/len(ratings_int)
        self.rating = ratings_sum
        self.save()
        return self.rating

    def count_reviews(self):
        return Review.objects.filter(product=self).count()


class Review(models.Model):
    class Star(models.IntegerChoices):
        STAR_ZERO = 0
        STAR_ONE = 1
        STAR_TWO = 2
        STAR_THREE = 3
        STAR_FOUR = 4
        STAR_FIVE = 5

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating_rev = models.PositiveSmallIntegerField(choices=Star.choices)
    data = models.DateTimeField(auto_now=True)
    text_rev = models.TextField(max_length=200)
    # author_rev = models.CharField(max_length=40)
    # comment_to_rev =

    def __str__(self):
        return self.text_rev[0:15] + '...'
