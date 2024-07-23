from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Healthcare', 'Healthcare'),
    ('Skincare', 'Skincare'),
    ('Cosmetics', 'Cosmetics'),
)


class Product(models.Model):
    # name = models.CharField(max_length=100, null=True)
    # quantity = models.PositiveIntegerField(null=True)
    # category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    price = models.FloatField(null=True)
    availability = models.IntegerField(null=True)
    number_of_products_sold = models.IntegerField(null=True)
    revenue_generated = models.FloatField(null=True)
    lead_times = models.IntegerField(null=True)
    order_quantities = models.IntegerField(null=True)
    shipping_times = models.IntegerField(null=True)
    shipping_costs = models.FloatField(null=True)
    location = models.CharField(max_length=100, null=True)
    production_volumes = models.IntegerField(null=True)
    manufacturing_lead_time = models.IntegerField(null=True)
    manufacturing_costs = models.FloatField(null=True)
    inspection_results = models.CharField(max_length=50, null=True)
    defect_rates = models.FloatField(null=True)
    costs = models.FloatField(null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'
