from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, default="Unknown")

    sales_price = models.FloatField(default=10.0)   # ✅ FIXED
    cost_price = models.FloatField(default=10.0)    # ✅ FIXED

    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField(default=10)         # ✅ FIXED

    whatsapp_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name