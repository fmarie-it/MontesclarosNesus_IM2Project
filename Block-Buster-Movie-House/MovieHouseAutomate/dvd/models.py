from django.db import models
from datetime import datetime, date

# Create your models here.
class DVD(models.Model):
    sku = models.AutoField(primary_key=True, verbose_name='SKU')
    date_registered = models.DateField(default=datetime.now, blank=True)
    genre = models.CharField(max_length = 100, null=False)
    title = models.CharField(max_length = 100, null=False)
    director_firstname = models.CharField(max_length = 100)
    director_lastname = models.CharField(max_length = 100)
    release_date = models.DateField()
    cast = models.CharField(max_length = 100)
    price = models.FloatField(default=0)
    no_items = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    #dimg = models.ImageField(default='NULL', upload_to="dvd_images/")
    dimg = models.ImageField(null=True, blank=True, upload_to="dvdPic/")

    class Meta:
        db_table = "DVD"
