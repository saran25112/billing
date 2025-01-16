from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Bill(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('account', 'Account (Credit)'),
    )

    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE)  # ForeignKey to Supplier
    item_name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=7, choices=PAYMENT_METHOD_CHOICES)
    customer_name = models.CharField(max_length=100)
    number_of_products = models.PositiveIntegerField()
    weight_in_kg = models.DecimalField(max_digits=5, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)  # Price per kg or item
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Total calculated later
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate total amount (number_of_products * weight_in_kg * rate)
        self.total_amount = self.number_of_products * self.weight_in_kg * self.rate
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill {self.id} - {self.customer_name}"
