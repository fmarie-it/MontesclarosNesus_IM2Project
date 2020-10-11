from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'dvd'
urlpatterns = [
    path('dvd-registration',views.DVDRegView.as_view(), name="adddvd_view"),
    #path('dvd-report',views.DVDReportView.as_view(), name="dvdreport_view"),
]

urlpatterns += staticfiles_urlpatterns() 