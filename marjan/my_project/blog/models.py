from django.db import models


class Author(models.Model):
    name = models.CharField("Имя автора", max_length=100)
    b_day = models.DateField("Дата рождения", auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Article(models.Model):
    title = models.CharField("Статья", max_length=200)
    text = models.TextField("Текст")
    create_d = models.DateField("Дата создания", auto_now=True)
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

