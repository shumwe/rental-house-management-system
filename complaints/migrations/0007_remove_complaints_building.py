# Generated by Django 4.0.2 on 2022-02-22 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0006_alter_complaints_body_alter_complaints_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='building',
        ),
    ]
