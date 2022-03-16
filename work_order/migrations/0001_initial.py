# Generated by Django 4.0.2 on 2022-03-11 16:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('complaints', '0011_alter_complaints_status'),
        ('accounts', '0004_alter_tenants_rented_unit'),
        ('rental_property', '0009_remove_maintanancenotice_unit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HiredPersonnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=55)),
                ('personnel_email', models.EmailField(max_length=155)),
                ('id_number', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('associated_account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_property.building')),
                ('personnel_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.managers')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('est_duration', models.CharField(max_length=70)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=20)),
                ('due_date', models.DateField()),
                ('additional_workers', models.ManyToManyField(related_name='other_workers', to='work_order.HiredPersonnel')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_order.hiredpersonnel')),
                ('parent_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complaints.unitreport')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental_property.rentalunit')),
            ],
        ),
    ]