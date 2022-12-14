from django.db import models
from vendor.models import Vendor

# Create your models here.

class Category(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    cateogory_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.catrgory_name


class FoodItems(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    cateogory = models.ForeignKey(Category, on_delete=models.CASCADE)
    food_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='foodimages')
    isavailable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Food Items'
    
    def __str__(self):
        return self.food_title