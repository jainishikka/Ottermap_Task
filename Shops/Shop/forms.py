from django import forms
from .models import Shop

class ShopRegistrationForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']
    
    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        if not (-90.0 <= latitude <= 90.0):
            raise forms.ValidationError('Latitude must be between -90 and 90 degrees.')
        return latitude
    
    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        if not (-180.0 <= longitude <= 180.0):
            raise forms.ValidationError('Longitude must be between -180 and 180 degrees.')
        return longitude
 
from django import forms
from decimal import Decimal

class LocationForm(forms.Form):
    latitude = forms.DecimalField(
        label='Latitude', 
        max_digits=9, 
        decimal_places=6, 
        min_value=Decimal('-90.000000'),
        max_value=Decimal('90.000000'),
        error_messages={
            'min_value': 'Latitude must be greater than -90.',
            'max_value': 'Latitude must be less than 90.'
        }
    )
    
    longitude = forms.DecimalField(
        label='Longitude', 
        max_digits=9, 
        decimal_places=6, 
        min_value=Decimal('-180.000000'),
        max_value=Decimal('180.000000'),
        error_messages={
            'min_value': 'Longitude must be greater than -180.',
            'max_value': 'Longitude must be less than 180.'
        }
    )

