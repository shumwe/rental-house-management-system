# Generated by Django 4.0.2 on 2022-03-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_order', '0003_hiredpersonnel_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiredpersonnel',
            name='personnel_code',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True),
        ),
    ]