# Generated by Django 3.2.3 on 2021-06-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210605_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
