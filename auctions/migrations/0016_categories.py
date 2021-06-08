# Generated by Django 3.2.3 on 2021-06-08 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20210606_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auction')),
            ],
        ),
    ]
