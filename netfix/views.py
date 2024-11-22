from django.shortcuts import render

from users.models import User, Company, Customer
from services.models import Service,RequestServiceModel


def home(request):
    return render(request, 'users/home.html', {'user': request.user})


def customer_profile(request,name):
    users= User.objects.get(username=name)
    sh = RequestServiceModel.objects.filter(
        Customer.objects.get(user=users)
    )
    return render(request, 'users/profile.html',{'users':users, 'name':name, 'sh':sh})

def company_profile(request, name):
    # fetches the company user and all of the services available by it
    user = User.objects.get(username=name)
    services = Service.objects.filter(
        company=Company.objects.get(user=user)).order_by("-date")

    return render(request, 'users/profile.html', {'user': user, 'services': services})
