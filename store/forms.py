from django import forms
from . models import Customer, Shipping


class CustomerForm(forms.ModelForm):
    """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
    class Meta:
        model = Customer
        fields = ('full_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',

        }
    #     taken from https://github.com/ckz8780/boutique_ado_v1/blob/         6b3837fb56fdb60655292badbb2dcf649a074ec7/checkout/forms.py

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class ShippiingForm(forms.ModelForm):
    """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
    class Meta:
        model = Shipping
        fields = ('country', 'postcode', 'town_or_city',
                  'street_address1', 'street_address2', 'county')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',

        }
    #     taken from https://github.com/ckz8780/boutique_ado_v1/blob/         6b3837fb56fdb60655292badbb2dcf649a074ec7/checkout/forms.py

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
