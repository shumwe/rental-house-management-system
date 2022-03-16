# Generated by Django 4.0.2 on 2022-03-13 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_tenants_rented_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenants',
            name='associated_account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='tenant'),
        ),
    ]