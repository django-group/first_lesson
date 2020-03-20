from django.db import models
from django.utils.text import slugify


class Charact(models.Model):
    # product = models.ManyToManyField(Product, verbose_name='Товар', blank=True)
    name = models.CharField('Характеристик', max_length=150)
    text = models.CharField('Значение', max_length=150)

    def __str__(self):
        return f'{self.name}: {self.text}'

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Product(models.Model):
    manufact = models.CharField('Производитель', null=False, blank=False, max_length=100)
    charact = models.ManyToManyField(Charact, verbose_name='Характеристики', blank=True)
    title = models.CharField("Название", max_length=150, blank=False, null=False)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    image = models.ImageField('Картинка', null=False, upload_to='mda/')
    description = models.TextField('Описание', max_length=500)
    # charact = models.ManyToManyField(Charact, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    avail = models.BooleanField('Наличие')
    # рейтинг
    # остаток
    # скидка
    asin = models.DecimalField('Код товара', max_digits=10, decimal_places=0)
    # гарантия


    def __str__(self):
        return f"{self.manufact} {self.title}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Reviews(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    data = models.DateTimeField('Дата отзыва', auto_now=True, editable=False)
    user = models.CharField('Пользователь', max_length=150, blank=True, null=False)
    text = models.TextField('Отзыв', max_length=1000, blank=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
