# Generated by Django 3.2.3 on 2021-06-05 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210605_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 5, 10, 2, 29, 315799)),
        ),
    ]
