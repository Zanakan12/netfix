from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="admin")
    birth = models.DateField(null=True, blank=True)
    
    def _str_(self):
        return self.user.username