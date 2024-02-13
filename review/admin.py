from django.contrib import admin
from .models import CustomerReview


# Register your models here.
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'comment','image')


admin.site.register(CustomerReview, CustomerReviewAdmin)
