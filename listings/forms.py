from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'address',
            'city',
            'state',
            'description',
            'price',
            'bedrooms',
            'bathrooms',
            'garage',
            'photo_main',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
            'photo_5',
            'photo_6',
            'realtor_name',
            'realtor_photo',
            'realtor_description',
            'realtor_phone',
            'realtor_email',
        ]



