from django.db import models
from datetime import datetime, date

# Create your models here.
class Person(models.Model):
    person_id = models.AutoField(primary_key=True, verbose_name='ID')
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=25)
    barangay = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    zip_code = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    birthdate = models.DateField(blank=True)
    status = models.CharField(max_length = 25)
    gender = models.CharField(max_length = 25)
    spouse_name = models.CharField(max_length = 100)
    spouse_occupation = models.CharField(max_length =100)
    no_children = models.IntegerField(default=0)
    #cimg = models.FileField(upload_to="customer_images/",default='NULL')
    cimg = models.ImageField(null=True, blank=True, upload_to="customerPic/")

    class Meta:
        db_table = "Person"

class Customer(Person):
    customer_id = models.AutoField(primary_key=True, verbose_name='Customer_ID')
    date_registered = models.DateField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "Customer"
