from django import forms

from users.models import Company
from users.forms import FIELD_CHOICE

class CreateNewService(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, label='Description')
    price_hour = forms.DecimalField(
    decimal_places=2, max_digits=5, min_value=0.00)
    
    field = forms.ChoiceField(required=True, choices=FIELD_CHOICE)

    def __init__(self, *args, choices='', ** kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        # adding choices to fields
        if choices:
            self.fields['field'].choices = choices
        # adding placeholders to form fields
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'

        self.fields['name'].widget.attrs['autocomplete'] = 'off'


class RequestServiceForm(forms.Form):
    address= forms.CharField(required=True)
    interval = forms.IntegerField(initial=2, required=True, min_value=1)

    def __init__(self, *args, choices='', ** kwargs):
        super(RequestServiceForm, self).__init__(*args, **kwargs)
        # adding placeholders to form fields
        self.fields['address'].widget.attrs['placeholder'] = 'Enter your address'
