from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 1:1
class Discount(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='discount')
    discount_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        help_text='Discount percentage (e.g., 10.00 for 10%)'
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.discount_percentage}% off for {self.product.name}'


# 1:N
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    user_id = models.PositiveBigIntegerField(max_length=50, blank=True, null=True)
    rating = models.PositiveIntegerField(default=1, help_text="Rating from 1 to 5")
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.product.name} by {self.user_id}'


# N:M
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    products = models.ManyToManyField(Product, related_name='categories', blank=True)

    def __str__(self):
        return self.name
