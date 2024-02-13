from django.urls import path 
from .views import signup, login
from dishes.views import dishes

urlpatterns = [
    # path('dishes/', dishes,name='dishes'),
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
]