from django.contrib import admin
from .models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('user','birth')
admin.site.register(Customer,CustomerAdmin)