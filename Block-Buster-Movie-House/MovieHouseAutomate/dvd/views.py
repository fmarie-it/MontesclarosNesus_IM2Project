from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse 
from .forms import DVDForm
from .models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here. Arrange in alphabetical order
class DVDRegView(View):
    def get(self, request):
        return render(request, 'dvd/dvdregis.html')

    def post(self, request):
        form = DVDForm(request.POST)
        if form.is_valid():

            genre = request.POST.get("genre")
            title = request.POST.get("title")
            director_firstname = request.POST.get("director_firstname")
            director_lastname = request.POST.get("director_lastname")
            release_date = request.POST.get("release_date")
            cast = request.POST.get("cast")
            price = request.POST.get("price")
            no_items = request.POST.get("no_items")
            dimg = request.FILES.get("dimg")

            form = DVD(director_firstname = director_firstname, director_lastname = director_lastname, genre = genre, 
            title = title, release_date = release_date, cast = cast, price = price, no_items = no_items, dimg = dimg)
            form.save()
            return HttpResponse('DVD recorded!')

        else:
            print(form.errors)
            return HttpResponse('Please fill all necessary information')


#class DVDReportView(View):
#    def get(self, request):
#        dvds = DVD.objects.all()
#        context = {
#            'title': 'DVD Dashboard',
#            'DVD' : dvds
#        }
#        return render(request, 'dvd/dvdreport.html', context)
