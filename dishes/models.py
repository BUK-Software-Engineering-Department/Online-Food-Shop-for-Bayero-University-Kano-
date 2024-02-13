from django.db import models
from django.conf import settings


# Create your models here.
class Dishe(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    item_description = models.TextField()
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to='static/dishes-image')

    def __str__(self):
        return self.name


class FoodType(models.Model):
    name = models.ForeignKey(Dishe, on_delete=models.CASCADE, related_name='product_name')
    CATEGORY_CHOICES = (
        ('drinks', 'Drinks'),
        ('gurasa', 'Gurasa'),
        ('meats', 'Meats'),
        ('pizza', 'Pizza'),
    )
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)


class RecommendProduct(models.Model):
    recommend_product = models.ForeignKey(Dishe, on_delete=models.CASCADE)


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dishes = models.ForeignKey('Dishe', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    # Add any additional fields you need, like quantity or timestamp

    def __str__(self):
        return f"{self.user.username} - {self.dishes.name}"
