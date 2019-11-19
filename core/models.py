from django.db import models

CATEGORY_CHOICES = (
    ('S', 'Shirt')
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

class OrderItem(models.Model):
    pass

class Order(models.Model):
    pass