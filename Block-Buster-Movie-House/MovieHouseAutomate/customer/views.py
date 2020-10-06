from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse 
from .forms import CustomerForm
from .models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from dvd.models import DVD

# Create your views here.Arrange in alphabetical order
class CustomerRegView(View):
    def get(self, request):
        return render(request, 'customer/customerregis.html')

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            
            fname = request.POST.get("firstname")
            lname = request.POST.get("lastname")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            street = request.POST.get("street")
            barangay = request.POST.get("barangay")
            city = request.POST.get("city")
            province = request.POST.get("province")
            zip_code = request.POST.get("zip_code")
            country = request.POST.get("country")
            birthdate = request.POST.get("birthdate")
            status = request.POST.get("status")
            gender = request.POST.get("gender")
            spouse_name = request.POST.get("spouse_name")
            spouse_occupation = request.POST.get("spouse_occupation")
            no_children = request.POST.get("no_children")
            cimg = request.FILES.get("cimg")

            form = Customer(firstname = fname, lastname = lname, phone = phone, email = email, street = street, barangay = barangay, city = city, 
            province = province, zip_code = zip_code, country = country, birthdate = birthdate, status = status, gender = gender, 
            spouse_name = spouse_name, spouse_occupation = spouse_occupation, no_children = no_children,
            cimg = cimg)
            form.save()
            return HttpResponse('Customer recorded!')

        else:
            print(form.errors)
            return HttpResponse('Please fill all necessary information')

class DashboardView(View):
    def get(self, request):
        customers = Customer.objects.all()
        dvds = DVD.objects.all()
        context = {
            'title': 'Dashboard',
            'customers' : customers,
            'DVD' : dvds
        }
        return render(request, 'customer/dashboard.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'customer_update' in request.POST:
                # this is for passing all the customer details from the modal in the html file.
                cid = request.POST.get("customer_id")
                fname = request.POST.get("firstname")
                lname = request.POST.get("lastname")
                phone = request.POST.get("phone")
                email = request.POST.get("email")
                street = request.POST.get("street")
                barangay = request.POST.get("barangay")
                city = request.POST.get("city")
                province = request.POST.get("province")
                zip_code = request.POST.get("zip_code")
                country = request.POST.get("country")
                birthdate = request.POST.get("bdate")
                status = request.POST.get("rel_status")
                gender = request.POST.get("gender")
                spouse_name = request.POST.get("spouse_name")
                spouse_occupation = request.POST.get("spouse_occupation")
                no_children = request.POST.get("no_children")
                cimg = request.POST.get("cimg")

                # and updating it to the database both customer and dvd respectively.
                update_customer = Customer.objects.filter(person_ptr_id = cid).update(firstname = fname, 
                lastname = lname, phone = phone, email = email, street = street, barangay = barangay, city = city, province = province,
                zip_code = zip_code, country = country, birthdate = birthdate, gender = gender, status = status,
                spouse_name = spouse_name, spouse_occupation = spouse_occupation, no_children = no_children, cimg = cimg)

                # printing it to the cmd for confirmation and for checking if it worked.
                print('Customer Details Updated Successfully!')

            # ------------------------------------------------------------------------------------------------- # 
            elif 'dvd_update' in request.POST:
                # this is for passing all the dvd details from the modal in the html file.
                sku = request.POST.get("sku")
                genre = request.POST.get("genre")
                title = request.POST.get("title")
                director_firstname = request.POST.get("director_firstname")
                director_lastname = request.POST.get("director_lastname")
                release_date = request.POST.get("release_date")
                cast = request.POST.get("cast")
                price = request.POST.get("price")
                no_items = request.POST.get("no_items")
                dimg = request.POST.get("dimg")

                # and updating it to the database both customer and dvd respectively.
                update_dvd = DVD.objects.filter(sku = sku).update(genre = genre, title = title, director_firstname = director_firstname,
                director_lastname = director_lastname, release_date = release_date, dimg = dimg, cast = cast,
                price = price, no_items = no_items)

                # printing it to the cmd for confirmation and for checking if it worked.
                print('DVD Details Updated Successfully!')

            # ------------------------------------------------------------------------------------------------- #          
            elif 'delete_customer' in request.POST:
                customer_id = request.POST.get("customer_id")
                delete_customer = Customer.objects.filter(person_ptr_id = customer_id).update(is_deleted = True)
                print('Entry deleted!')

            # ------------------------------------------------------------------------------------------------- # 
            elif 'delete_dvd' in request.POST:
                sku = request.POST.get("sku")
                delete_dvd = DVD.objects.filter(sku = sku).update(is_deleted = True)
                print('Entry deleted!')

        return redirect('customer:dashboard_view')