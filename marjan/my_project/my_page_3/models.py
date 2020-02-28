from django.db import models


class Author(models.Model):
    name = models.CharField("Имя автора", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Books(models.Model):
    name = models.CharField("Книга", max_length=50)
    genre = models.CharField("Жанр", max_length=50)
    description = models.TextField("Описание")
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
