from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import UserManager



class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    birth=models.DateField(null=True, default='2000-01-01')
    email = models.CharField(max_length=100, unique=True)

class Customer(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth = models.DateField(null=True, default='2000-01-01')
    email = models.EmailField(null=False, default='rafta@test.com')

    def __str__(self):
        return str(self.user.id) + ' - ' + self.user.username


class Company(models.Model):
    user = models.OneToOneField(
    User, on_delete=models.CASCADE, primary_key=True)
    field = models.CharField(max_length=70, choices=(('Air Conditioner', 'Air Conditioner'),
                                                     ('All in One', 'All in One'),
                                                     ('Carpentry', 'Carpentry'),
                                                     ('Electricity',
                                                      'Electricity'),
                                                     ('Gardening', 'Gardening'),
                                                     ('Home Machines',
                                                      'Home Machines'),
                                                     ('House Keeping',
                                                      'House Keeping'),
                                                     ('Interior Design',
                                                      'Interior Design'),
                                                     ('Locks', 'Locks'),
                                                     ('Painting', 'Painting'),
                                                     ('Plumbing', 'Plumbing'),
                                                     ('Water Heaters', 'Water Heaters')), blank=False, null=False)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)

    def __str__(self):
        return str(self.user.id) + ' - ' + self.user.username
