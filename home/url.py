from django.urls import path
from .views import index
from dishes.views import dishes

urlpatterns = [
    path('', index, name='home'),
    path('/dishes',name='dishes')
]
