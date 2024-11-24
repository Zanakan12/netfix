from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from users.models import Company, Customer, User
from .models import Service, RequestServiceModel
from .forms import CreateNewService, RequestServiceForm
from django.contrib import messages
from netfix.settings import FIELD_CHOICE

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

def service_list(request):
    service_list = Service.objects.all().order_by("-date")  # Récupère tous les services, triés par date décroissante
    paginator = Paginator(service_list, 7)  # Affiche 5 services par page

    page_number = request.GET.get('page')  # Récupère le numéro de page depuis les paramètres de l'URL

    try:
        services = paginator.page(page_number)
    except PageNotAnInteger:
        # Si le numéro de page n'est pas un entier, affiche la première page
        services = paginator.page(1)
    except EmptyPage:
        # Si le numéro de page est trop élevé, affiche la dernière page disponible
        services = paginator.page(paginator.num_pages)

    context = {
        'services': services  # 'services' est maintenant un objet Page contenant les services de la page courante
    }

    return render(request, 'services/list.html', context)



def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})


def create(request):
    user_id = request.user.id
    company_instance = Company.objects.get(user_id=user_id)
    company_type = company_instance.field  # Supposons que le nom de la compagnie est dans le champ `name`

    if request.method == 'POST':
        form = CreateNewService(request.POST, choices=FIELD_CHOICE, company_type=company_type)
        if form.is_valid():
            Service.objects.create(
                company=company_instance,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price_hour=form.cleaned_data['price_hour'],
                field=form.cleaned_data['field']
            )
            form = CreateNewService(choices=FIELD_CHOICE, company_type=company_type)
    else:
        form = CreateNewService(choices=FIELD_CHOICE, company_type=company_type)

    return render(request, 'services/create.html', {'form': form})


def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})




@login_required
def request_service(request, id):
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(Customer, pk=request.user.id)
            customer = get_object_or_404(Customer, user=request.user)
            service = Service.objects.get(id=id)
            name = customer.user.username
            company = service.company.user
            custom_field= service.field
            description = service.description
            job_name= service.name
            service.nb_request += 1
            service.save()
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
            form=RequestServiceForm()
    else:
        form = RequestServiceForm()
    return render(request, 'services/request_service.html', {'form': form})

def most_requested(request):
    services = Service.objects.order_by('-nb_request')[:3]
    return render(request,'services/most_requested.html',{'services':services})

@login_required
def rating(request,id):
    service = get_object_or_404(Service,id=id )
    if request.method=='POST':
        service.nb_client_rating += 1
        service.nb_total_rating += int(request.POST.get('rating',0))
        service.rating = service.nb_total_rating/service.nb_client_rating
        service.save()
    return render(request, 'services/rating.html',{'service':service})