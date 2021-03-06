# Generated by Django 4.0.2 on 2022-03-09 12:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_servicerating_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerating',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Rate us on a scale of 1 to 10'),
        ),
    ]
