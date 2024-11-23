from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import User, Company, Customer


FIELD_CHOICE = (('air-conditioner', 'Air Conditioner'),
                ('carpentry', 'Carpentry'),
                ('electricity', 'Electricity'),
                ('gardening', 'Gardening'),
                ('home-machines', 'Home Machines'),
                ('house-keeping', 'House Keeping'),
                ('interior-design', 'Interior Design'),
                ('locks', 'Locks'),
                ('painting', 'Painting'),
                ('plumbing', 'Plumbing'),
                ('water-heaters', 'Water Heaters'))

class DateInput(forms.DateInput):
    input_type = 'date'


def validate_email(value):
    # In case the email already exists in an email input in a registration form, this function is fired
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            value + " is already taken.")


class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    field = forms.ChoiceField(choices=FIELD_CHOICE)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Validation password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_company=True
        if commit:
            #user.is_company = True
            user.save()
            # Création de l'objet Company lié avec `field` et non `field_of_work`
            Company.objects.create(
                user=user,
                field=self.cleaned_data['field'],  # Correspond au champ `field` dans le modèle
            )
        return user

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required= True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Validation password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','birth']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet e-mail est déjà utilisé.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur est déjà pris.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_customer = True
        if commit:
            user.save()
            Customer.objects.create(
                user=user,
            )
        return user

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom d’utilisateur'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
    )