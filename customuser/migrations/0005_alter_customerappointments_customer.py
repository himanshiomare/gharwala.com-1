# Generated by Django 4.0.4 on 2022-05-29 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0004_alter_profile_desc_alter_profile_locations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerappointments',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
