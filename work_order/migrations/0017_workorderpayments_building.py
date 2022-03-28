# Generated by Django 4.0.2 on 2022-03-23 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_property', '0015_alter_maintanancenotice_maintanance_status'),
        ('work_order', '0016_alter_workorder_email_personnel'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorderpayments',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental_property.building'),
        ),
    ]