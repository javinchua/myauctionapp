# Generated by Django 3.2.3 on 2021-06-02 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210528_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 8, 25, 37, 21536)),
        ),
    ]
