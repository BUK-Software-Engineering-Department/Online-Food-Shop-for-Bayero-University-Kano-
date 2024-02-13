from django.db import models


# Create your models here.
class CustomerReview(models.Model):
    name = models.CharField(max_length=200)
    rate = models.IntegerField()
    comment = models.TextField()
    image = models.ImageField(upload_to='static/review-images',null=True,blank=True)
