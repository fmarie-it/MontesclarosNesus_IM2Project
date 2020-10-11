from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse 
from .forms import OrdersForm
from dvd.models import DVD
from customer.models import Customer
from .models import *
from django.conf import settings

# Create your views here. Arrange in alphabetical order
class OrdersRegView(View):
    def get(self, request):
        return render(request, 'orders/orders.html')

    def post(self, request):
        newObject = OrdersForm(request.POST)
        if newObject.is_valid():
            # requesting the entries from the html.
            customer_first = request.POST.get("customer_first")
            customer_last = request.POST.get("customer_last")
            title = request.POST.get("title")
            quantity = request.POST.get("quantity")
            phone = request.POST.get("phone")
            email = request.POST.get("email")

            getCustomer = Customer.objects.filter(firstname = customer_first, lastname = customer_last).first()
            getDVD = DVD.objects.filter(title = title).first()

            print('passed here')
            print(getCustomer)
            print(getDVD)

            # checking if both customer and dvd exist.
            if getCustomer is not None and getDVD is not None:
                # creating the new order.
                newObject = Order(customer_first=customer_first, customer_last=customer_last, dvd_title=title,
                quantity=quantity, phone=phone, email=email)
                newObject.save()
                return HttpResponse('Order added!')
        
        else:
            print(newObject.errors)
            return HttpResponse('Please fill all necessary information so we can provide the best service possible.')
        return redirect('orders:orders_view')

class OrdersView(View):
    def get(self, request):
        orders = Order.objects.all()
        context = {
            'title': 'Orders',
            'Orders' : orders,
        }
        return render(request, 'orders/orderstable.html', context)

    # def post(self, request):