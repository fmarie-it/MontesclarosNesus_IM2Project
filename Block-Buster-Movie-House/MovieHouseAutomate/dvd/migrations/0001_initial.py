# Generated by Django 3.1.1 on 2020-10-01 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('sku', models.AutoField(primary_key=True, serialize=False, verbose_name='SKU')),
                ('date_registered', models.DateField(blank=True, default=datetime.datetime.now)),
                ('genre', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('director_firstname', models.CharField(max_length=100)),
                ('director_lastname', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('cast', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('no_items', models.IntegerField(default=0)),
                ('is_deleted', models.BooleanField(default=False)),
                ('dimg', models.ImageField(default='NULL', upload_to='dvd_images/')),
            ],
            options={
                'db_table': 'DVD',
            },
        ),
    ]
