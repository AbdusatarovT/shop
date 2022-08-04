from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from applications.product.models import Product

User = get_user_model()

class Order(models.Model):
    CART_SATUS = (
        ('in_processing', 'in_processing'),  # В процессе
        ('completed', 'completed'),  # Завершенный
        ('declined', 'declined')  # Отмененный
    )

    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='orders')
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # quantity = models.PositiveIntegerField()
    status = models.CharField(choices=CART_SATUS, max_length=20, default='in_processing')

    address = models.TextField()
    number = models.TextField()
    first_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} ordered'


    # def save(self, *args, **kwargs):
    #     self.total_cost = self.product.price * self.quantity
    #     super().save(*args, **kwargs)


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)


    def __str__(self):
        return self.user.email


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.cart.id} {self.product}'


    def save(self, *args, **kwargs):
        self.total_cost = self.product.price * self.quantity
        try:
            cartitem = CartItem.objects.get(id=self.id)
            cartitem.cart.total_cost = cartitem.cart.total_cost - cartitem.cart.total_cost + self.total_cost
            cartitem.cart.save()

        except CartItem.DoesNotExist:
            self.cart.total_cost += self.total_cost
            self.cart.save()

        super(CartItem, self).save()

# сгнал который сробаьывает когда удоляется продукт
@receiver(post_delete, sender=CartItem)
def delete_signal(sender, instance, **kwargs):
    print('DELETE')
    instance.cart.total_cost -= instance.total_cost
    instance.cart.save()

