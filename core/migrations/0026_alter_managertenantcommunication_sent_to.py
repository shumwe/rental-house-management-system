# Generated by Django 4.0.2 on 2022-03-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_tenants_rented_unit'),
        ('core', '0025_managertenantcommunication_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managertenantcommunication',
            name='sent_to',
            field=models.ManyToManyField(to='accounts.Tenants'),
        ),
    ]
