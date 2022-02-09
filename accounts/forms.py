from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):

    class Meta:
        model = UserAccount
        fields = (
            'full_name', 'email', 'phone_number',
            'shipping_street_name', 'shipping_street_number',
            'shipping_town_or_city', 'shipping_county', 'shipping_postcode',
            'shipping_country', 'billing_street_name', 'billing_street_number',
            'billing_town_or_city', 'billing_county', 'billing_postcode',
            'billing_country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone number',
            'email': 'Email Address',
            'shipping_street_name': 'Shipping street address 1',
            'shipping_street_number': 'Shipping street address 2',
            'shipping_town_or_city': 'Shipping Town or City',
            'shipping_county': 'Shipping County, State or Locality',
            'shipping_postcode': 'Shipping postal code',
            'billing_street_name': 'Billing street address 1',
            'billing_street_number': 'Billing street address 2',
            'billing_town_or_city': 'Billing Town or City',
            'billing_county': 'Billing County, State or Locality',
            'billing_postcode': 'Billing Postal code',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'shipping_country' and field != 'billing_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
