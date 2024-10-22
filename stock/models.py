from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Laboratories"

    def __str__(self):
        return self.lab_name

class Products(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True)
    unit_of_issue = models.CharField(max_length=20, default='DEFAULT_UNIT')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"
    def __str__(self):
        return f'{self.item_name} - {self.quantity}'

class Transaction(models.Model):
    PRODUCT_ACTIONS = (
        ('RECEIVE', 'Receive'),
        ('ISSUE', 'Issue'),
    )
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=PRODUCT_ACTIONS)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f'{self.product.item_name} - {self.action} - {self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order of {self.product.item_name} by {self.staff.username} on {self.date}'
