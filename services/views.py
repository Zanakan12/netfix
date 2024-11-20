from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from users.models import Company, Customer, User

from .models import Service
from .forms import CreateNewService, RequestServiceForm
from django.contrib import messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})


def create(request):
    if request.method == 'POST':
        form=CreateNewService(request.POST)
        user_id = request.user.id
        if form.is_valid():
            company_instance = Company.objects.get(user_id=user_id)
            Service.objects.create(
                company=company_instance,
                name= form.cleaned_data['name'],
                description= form.cleaned_data['description'],
                price_hour= form.cleaned_data['price_hour']
            )
        messages.success(request, "Votre service a été crée avec succès !")
    else:
        form=CreateNewService
    return render(request, 'services/create.html',{'form':form})

def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


def request_service(request, id):
    return render(request, 'services/request_service.html', {})
