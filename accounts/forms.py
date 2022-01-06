from django import forms
from .models import Users


class UserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone number',
            'shipping_street_address1': 'Shipping street address 1',
            'shipping_street_address2': 'Shipping street address 2',
            'shipping_town_or_city': 'Shipping Town or City',
            'shipping_county': 'Shipping County, State or Locality',
            'shipping_postcode': 'Shipping postal code',
            'billing_street_address1': 'Billing street address 1',
            'billing_street_address2': 'Billing street address 2',
            'billing_town_or_city': 'Billing Town or City',
            'billing_county': 'Billing County, State or Locality',
            'billing_postcode': 'Billing Postal code',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'shipping_country' | field != 'billing_country'  :
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
