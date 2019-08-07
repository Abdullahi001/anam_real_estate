from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta(object):
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
            'realtor_phone',
            'realtor_email',
        ]
        widgets = {
        'title': forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            ),
        'address': forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            ),
        'city': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'state': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'description': forms.Textarea(
        attrs={
            'class': 'form-control'
            }
        ),
        'price': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'bedrooms': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'bathrooms': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'garage': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'realtor_name': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'realtor_description': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'realtor_phone': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        'realtor_email': forms.TextInput(
        attrs={
            'class': 'form-control'
            }
        ),
        }


