from django.contrib import admin
from djstore import models

# Register your models here.


admin.site.register(models.Product)
admin.site.register(models.Review)
admin.site.register(models.Categorie)