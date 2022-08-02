from django.contrib import admin

from applications.cart.models import *


admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)