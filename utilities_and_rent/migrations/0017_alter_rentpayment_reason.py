# Generated by Django 4.0.2 on 2022-02-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0016_unitrentdetails_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentpayment',
            name='reason',
            field=models.TextField(blank=True, help_text='If rejected...Reason..', null=True),
        ),
    ]
