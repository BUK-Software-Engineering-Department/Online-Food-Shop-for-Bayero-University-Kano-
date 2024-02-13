from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import reviews,add_review
urlpatterns = [
    path('', reviews, name='review'),
    path('add/',add_review,name='customer_review')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)