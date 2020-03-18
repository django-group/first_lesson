from django.contrib import admin
from main_page import models

admin.site.register(models.Specification)
admin.site.register(models.Product)
admin.site.register(models.Review)


# class ProductAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#     list_display = [field.title for field in models.Product._meta.fields]
#     fields = ['title', 'amount']
#     list_filter = ['title']
#     search_fields = ['title']
#
#     class Meta:
#         model = models.Product
