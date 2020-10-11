from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'orders'
urlpatterns = [
    path('orders',views.OrdersRegView.as_view(), name="orders_view"),
    path('orderstable',views.OrdersView.as_view(), name="orderstable_view"),
]

urlpatterns += staticfiles_urlpatterns() 