# Generated by Django 4.0.2 on 2022-03-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_order', '0017_workorderpayments_building'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workorderpayments',
            options={'verbose_name': 'Payments', 'verbose_name_plural': 'Payments'},
        ),
        migrations.AlterField(
            model_name='workorderpayments',
            name='payment_date',
            field=models.DateTimeField(),
        ),
    ]
