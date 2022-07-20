from django.contrib import admin
from .models import Category, Product, Image




admin.site.register(Category)
# admin.site.register(Product, ProductAdmin)
admin.site.register(Image)



class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


class ProductAdmin(admin.ModelAdmin): # для соединение картинки и продускта
    inlines = [ImageInAdmin]



admin.site.register(Product, ProductAdmin)