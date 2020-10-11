from django.db import models
from datetime import datetime, date

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='order_id')
    customer_first = models.CharField(max_length=20, default="")
    customer_last = models.CharField(max_length=20, default="")
    dvd_title = models.CharField(max_length=30)
    order_date = models.DateField(default=datetime.now, blank=True)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)
    sent = models.BooleanField(default=False)

    class Meta:
        db_table = "Order"


