from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email' ,'shipping_street_name', 'shipping_street_number',
                  'shipping_town_or_city', 'shipping_county',
                  'shipping_postcode', 'shipping_country','billing_street_name',
                  'billing_street_number', 'billing_town_or_city', 'billing_county',
                  'billing_postcode', 'billing_country')


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'shipping_street_name': '(Shipping) Street Name',
            'shipping_street_number': '(Shipping) Street Number', 
            'shipping_town_or_city': '(Shipping) Town or City', 
            'shipping_county': '(Shipping) County, State or Locality', 
            'shipping_postcode': '(Shipping) Postal code', 
            'shipping_country': '(Shipping) Country',
            'billing_street_name': '(Billing) Street name',
            'billing_street_number': '(Billing) Street Number', 
            'billing_town_or_city': '(Billing) Town or City', 
            'billing_county': '(Billing) County, State or Locality', 
            'billing_postcode': '(Billing) Postal code', 
            'billing_country': '(Billing) Country',
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
