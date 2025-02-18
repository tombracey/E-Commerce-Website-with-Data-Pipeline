from django.db import models
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    # image = models.ImageField(upload_to='pages/products/', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# class Customer(models.Model):
#     first_name = models.CharField(max_length=35)
#     last_name = models.CharField(max_length=35)
#     email = models.EmailField(unique=True)
#     shipping_address = models.TextField()
#     billing_address = models.TextField()

#     def __str__(self):
#         return self.first_name + " " + self.last_name
    
class ContactUs(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"

