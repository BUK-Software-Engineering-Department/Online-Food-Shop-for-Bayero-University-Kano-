from django.urls import path
from . import views
from .views import product_list_by_category,search_products,cart,add_to_cart


urlpatterns = [
    path('', views.dishes, name='dishes'),
    path('dishes/<str:category>/', product_list_by_category, name='product_list_by_category'),
    path('search/', search_products, name='search_products'),
    path('cart/', cart, name='cart'),
    path('<int:id>/', add_to_cart, name='add_to_cart'),



]