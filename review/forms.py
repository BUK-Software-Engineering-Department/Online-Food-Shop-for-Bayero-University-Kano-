from django import forms
from django.forms import NumberInput, TextInput,Textarea,IntegerField
from .models import CustomerReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview

        fields = [
            'name',
            'rate',
            'comment',
            'image',

        ]
        widgets = {
            'name': TextInput(attrs={'class': 'container', 'placeholder': 'name'}),
            'rate': NumberInput(attrs={'class': 'container', 'placeholder': 'rate','label':'Rate'}),
            'comment': Textarea(attrs={'class': 'container', 'placeholder': 'Describe your experience(optional)'}),
        }

