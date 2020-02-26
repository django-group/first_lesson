from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_birth = models.DateField(auto_now=False)

    def __str__(self):
        return self.name + " " + self.surname


class Book(models.Model):
    CHOISE_GANRE = (
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('cooking', 'Cooking'),
        ('technical', 'Technical'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    discribe = models.TextField(max_length=2000)
    enter_date = models.DateField(auto_now=False)
    genre = models.CharField(max_length=50, choices=CHOISE_GANRE)

    def __str__(self):
        return self.title