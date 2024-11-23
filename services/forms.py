from django import forms

from users.models import Company
from users.forms import FIELD_CHOICE
from netfix.settings import COMPANY_CHOICES_MAPPING

class CreateNewService(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, label='Description')
    price_hour = forms.DecimalField(
        decimal_places=2, max_digits=5, min_value=0.00
    )
    field = forms.ChoiceField(required=True, choices=[])

    def __init__(self, *args, choices=None, company_type=None, **kwargs):
        # Supprimez `company_name` de kwargs pour éviter une erreur
        kwargs.pop('company_name', None)
        super(CreateNewService, self).__init__(*args, **kwargs)


        # Appliquer les choix spécifiques à la compagnie
        if company_type in COMPANY_CHOICES_MAPPING:
            choices = COMPANY_CHOICES_MAPPING[company_type]

        # Définir les choix dans le champ `field`
        self.fields['field'].choices = choices

        # Ajout des placeholders et des attributs HTML
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'
        self.fields['name'].widget.attrs['autocomplete'] = 'off'

        # Définir une valeur par défaut si un seul choix est disponible
        if len(choices) == 1:
            self.fields['field'].initial = choices[0][0]


class RequestServiceForm(forms.Form):
    address= forms.CharField(required=True)
    interval = forms.IntegerField(initial=2, required=True, min_value=1)

    def __init__(self, *args, choices='', ** kwargs):
        super(RequestServiceForm, self).__init__(*args, **kwargs)
        # adding placeholders to form fields
        self.fields['address'].widget.attrs['placeholder'] = 'Enter your address'
