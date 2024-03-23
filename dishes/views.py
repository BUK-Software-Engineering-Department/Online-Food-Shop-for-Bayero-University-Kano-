from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dishe
from django.urls import reverse
from django.db.models import Q, Sum
from .models import FoodType, RecommendProduct, CartItem
from . import models

# Create your views here.
def dishes(request):
    products = Dishe.objects.all()
    trending = FoodType.objects.all()
    recommend_item = RecommendProduct.objects.all()
    context = {'dishes': products, 'trending': trending, 'recommend_item': recommend_item}
    return render(request, 'dishes.html', context)


def product_list_by_category(request, category):
    products = FoodType.objects.filter(category=category)
    return render(request, 'product_list_by_category.html', {'dishes': products, 'category': category})


def search_products(request):
    query = request.GET.get('key', '')
    products = Dishe.objects.filter(Q(name__icontains=query) | Q(name__iexact=query))
    return render(request, 'search_results.html', {'dishes': products, 'query': query})

@login_required
def add_to_cart(request, id):
    dishes = get_object_or_404(Dishe, id=id)
    user = request.user
    # Filter cart items for the user and dishes
    cart_items = CartItem.objects.filter(user=user, dishes=dishes)
    if cart_items.exists():
        # If there are existing cart items for the dishes, increment the quantity
        cart_item = cart_items.first()
        cart_item.quantity += 1
        # cart_item.save()
    else:
        # If there are no existing cart items, create a new one
        cart_item = CartItem(user=user, dishes=dishes, quantity=1)
        cart_item.save()

    # Calculate the cart count
    if request.user.is_authenticated:
        dishes = Dishe.objects.get(id=id)
        # Create and save the new CartItem instance
        cart_item = CartItem(user=request.user, dishes=dishes)
        cart_item.save()
        cart_count = CartItem.objects.filter(user=user).count()
        # Return the updated count in a JSON response
        return JsonResponse({'cart_count': cart_count})
    return redirect('dishes')


def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.dishes.price for item in cart_items)
    else:
        cart_items = []
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def checkout_order(request):
    # get all the cart items
    cart_items = request.user.cartitem_set.all()

    if cart_items.count():
        # first create an order
        order = models.CartItem.objects.create(user=request.user)

        # replicate the cart items to order items and delete them from the cart
        # for item in cart_items:
        #     models.CartItem.objects.create(
        #         order = order, product=item.name, amount=item.quantity, price=item.dishes.price
        #     )
        for item in cart_items:
            if item.dishes:  # Check if 'dishes' exists
                price = item.dishes.price
            else:
                # Handle the case where 'dishes' is missing (e.g., set default price, log an error)
                price = 0.0  # Set a default price (adjust as needed)
                # You might want to log an error or take other actions based on your specific requirements
                print(f"Error: Item {item.name} has no 'dishes' attribute")

            models.CartItem.objects.create(
                order=order,
                product=item.name,
                amount=item.quantity,
                price=price
            )

            item.delete()
    
    return redirect("dishes:order_summary")
