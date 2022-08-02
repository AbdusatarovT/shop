from django.contrib.auth import get_user_model
from django.db import models

from applications.product.models import Product

User = get_user_model()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='orders')
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.product} ordered'


    def save(self, *args, **kwargs):
        self.total_cost = self.product.price * self.quantity
        super().save(*args, **kwargs)


class Cart(models.Model):
    CART_SATUS = (
        ('in_processing', 'in_processing'), # В процессе
        ('completed', 'completed'), # Завершенный
        ('declined', 'declined') # Отмененный
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    status = models.CharField(choices=CART_SATUS, max_length=20, default='in_processing')

    def __str__(self):
        return self.user.email


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField(default=1)
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.cart.id} {self.product}'


    def save(self, *args, **kwargs):
        self.total_cost = self.product.price * self.quantity
        super(CartItem, self).save()