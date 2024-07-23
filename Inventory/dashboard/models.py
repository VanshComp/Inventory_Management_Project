from django.db import models
from django.contrib.auth.models import User
from import_export import resources

# Create your models here.
CATEGORY = (
    ('Healthcare', 'Healthcare'),
    ('Skincare', 'Skincare'),
    ('Cosmetics', 'Cosmetics'),
)

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    # Primary Key
    id = models.AutoField(primary_key=True)

    # Foreign Key for Location
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    category = models.CharField(max_length=50, choices=CATEGORY)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    availability = models.IntegerField()
    number_of_products_sold = models.IntegerField()
    revenue_generated = models.FloatField()
    lead_times = models.IntegerField()
    order_quantities = models.IntegerField()
    shipping_times = models.IntegerField()
    shipping_costs = models.FloatField()
    production_volumes = models.IntegerField()
    manufacturing_lead_time = models.IntegerField()
    manufacturing_costs = models.FloatField()
    inspection_results = models.CharField(max_length=50)
    defect_rates = models.FloatField()
    costs = models.FloatField()

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    # Primary Key
    id = models.AutoField(primary_key=True)

    # Foreign Key for Product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Foreign Key for User
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    order_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.customer}-{self.product}' 