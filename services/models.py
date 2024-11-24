from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Company, Customer
from netfix.settings import FIELD_CHOICE

class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price_hour = models.DecimalField(decimal_places=2, max_digits=100)
    rating = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(5)], default=0)
    nb_client_rating = models.IntegerField(default=0, null=False)
    nb_total_rating= models.IntegerField(default=0, null=False)
    choices = FIELD_CHOICE
    field = models.CharField(max_length=30, blank=False,
                             null=False, choices=choices)
    date = models.DateTimeField(auto_now=True, null=False)
    nb_request=models.IntegerField(default=0, null=False)
    def __str__(self):
        return self.name


class RequestServiceModel(models.Model):
    name = models.CharField(max_length=50, null=False, default='rafta')
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.CharField(max_length=50, null=False, default='Default Company')
    job_name = models.CharField(max_length=50, null=False, default='Masson')
    service_id = models.IntegerField(default=0)
    custom_field = models.CharField(max_length= 50, null= False, default='souillon')
    address = models.CharField(max_length=50, null=False)
    interval= models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(8)], default=0)
    salary = models.IntegerField(default=0)
    description= models.CharField(max_length=150, null=False, default='nothing here')
    request_date = models.DateTimeField(auto_now=True, null=False)
    
    