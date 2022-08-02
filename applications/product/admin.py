from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Rating)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5

class CommentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'text', 'product', 'created_at']
    list_filter = ['created_at']
    search_fields = ['owner']

class ProductAdmin(admin.ModelAdmin): # для соединение картинки и продускта
    inlines = [ImageInAdmin]
    list_display = ['id', 'name', 'price', 'count_like']

    def count_like(self, obj):
        return obj.likes.filter(like=True).count()



admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
