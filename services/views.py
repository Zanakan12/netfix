from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from users.models import Company, Customer, User

from .models import Service, RequestServiceModel
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
    service= Service.objects.all()
    return render(request, 'services/list.html', {'services': services, 'service':service})


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
                price_hour= form.cleaned_data['price_hour'],
                field=form.cleaned_data['field']
            )
        messages.success(request, "Votre service a été crée avec succès !")
        return render(request,'services/field.html')
    else:
        form=CreateNewService
    return render(request, 'services/create.html',{'form':form})

def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


from django.shortcuts import get_object_or_404

def request_service(request, id):
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(Customer, pk=request.user.id)
            customer = get_object_or_404(Customer, user=request.user)
            #company = get_object_or_404(Company, user=request.user)
            service = Service.objects.get(id=id)
            name = customer.user.username
            company = service.company.user
            custom_field= service.field
            description = service.description
            job_name= service.name
            RequestServiceModel.objects.create(
                user_id=user,
                service_id=id,
                address=form.cleaned_data['address'],
                interval=form.cleaned_data['interval'],
                name = name,
                company = company,
                custom_field= custom_field,
                description = description,
                salary=form.cleaned_data['interval']*service.price_hour,
                job_name = job_name
            )
    else:
        form = RequestServiceForm()
    return render(request, 'services/request_service.html', {'form': form})
