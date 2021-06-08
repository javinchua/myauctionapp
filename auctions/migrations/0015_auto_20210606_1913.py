# Generated by Django 3.2.3 on 2021-06-06 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_auction_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='my_winnings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='current_winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='my_leadings', to=settings.AUTH_USER_MODEL),
        ),
    ]
