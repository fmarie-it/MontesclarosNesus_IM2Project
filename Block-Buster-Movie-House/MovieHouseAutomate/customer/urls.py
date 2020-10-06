#from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'customer'
urlpatterns = [
    path('customer-registration',views.CustomerRegView.as_view(), name="addcustomer_view"),
    path('dashboard',views.DashboardView.as_view(), name="dashboard_view"),
    
]

urlpatterns += staticfiles_urlpatterns() 