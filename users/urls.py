from django.urls import path
from django.contrib.auth import views
from . import views as v

urlpatterns = [
    path('', v.register, name='register'),
    path('company/', v.CompanySignUpView.as_view(), name='register_company'),
    path('customer/', v.CustomerSignUpView.as_view(), name='register_customer'),
    #path('login/', v.LoginUserView, name='login_user'),
    path('login/',v.CustomLoginView.as_view(),name='login')
]
