from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver

from .forms import CustomerSignUpForm, CompanySignUpForm,CustomLoginForm
from .models import User, Company, Customer
from netfix import settings

def register(request):
    return render(request, 'users/register.html')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/register_customer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'users/register_company.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # Spécifiez le template pour la connexion
    authentication_form = CustomLoginForm  # Utilisez le formulaire personnalisé
    
@receiver(social_account_added)
def set_user_as_customer(sender, request, sociallogin, **kwargs):
    # Récupérer l'utilisateur qui vient de se connecter
    user = sociallogin.user
    print(user)
    # Vérifier si la connexion provient de Google
    if sociallogin.account.provider == 'google':
        # Attribuer le rôle de customer
        user.is_customer = True
        user.save()