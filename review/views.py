from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import CustomerReview
from .forms import ReviewForm


# Create your views here.
def reviews(request):
    review = CustomerReview.objects.all()
    return render(request, 'review.html', {'review': review})


def add_review(request):
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST,request.FILES)
        print('Add review')
        if review_form.is_valid():
            review_form.save()
            return redirect('review')
    else:
        print('something wrong')
    context = {
        "review_form": review_form
    }
    return render(request, 'add_review.html', context)