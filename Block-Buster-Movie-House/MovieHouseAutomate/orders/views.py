from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse 
#from .forms import OrderForm
from .models import *
from django.conf import settings

# Create your views here.Arrange in alphabetical order
class OrdersView(View):
    def get(self, request):
        return render(request, 'orders/orders.html')

    # def post(self, request):
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
            
    #         fname = request.POST.get("firstname")
    #         lname = request.POST.get("lastname")
    #         phone = request.POST.get("phone")
    #         email = request.POST.get("email")
    #         street = request.POST.get("street")
    #         barangay = request.POST.get("barangay")
    #         city = request.POST.get("city")
    #         province = request.POST.get("province")
    #         zip_code = request.POST.get("zip_code")
    #         country = request.POST.get("country")
    #         birthdate = request.POST.get("birthdate")
    #         status = request.POST.get("status")
    #         gender = request.POST.get("gender")
    #         spouse_name = request.POST.get("spouse_name")
    #         spouse_occupation = request.POST.get("spouse_occupation")
    #         no_children = request.POST.get("no_children")
    #         cimg = request.FILES.get("cimg")

    #         form = Customer(firstname = fname, lastname = lname, phone = phone, email = email, street = street, barangay = barangay, city = city, 
    #         province = province, zip_code = zip_code, country = country, birthdate = birthdate, status = status, gender = gender, 
    #         spouse_name = spouse_name, spouse_occupation = spouse_occupation, no_children = no_children,
    #         cimg = cimg)
    #         form.save()
    #         return HttpResponse('Customer recorded!')

    #     else:
    #         print(form.errors)
    #         return HttpResponse('Please fill all necessary information')
