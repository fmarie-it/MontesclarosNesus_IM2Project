#from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'orders'
urlpatterns = [
    path('orders',views.OrdersView.as_view(), name="orders_view"),
    #path('dashboard',views.DashboardView.as_view(), name="dashboard_view"),
]

urlpatterns += staticfiles_urlpatterns() 