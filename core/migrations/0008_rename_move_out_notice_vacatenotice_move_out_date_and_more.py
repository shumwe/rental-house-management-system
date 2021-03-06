# Generated by Django 4.0.2 on 2022-02-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_evictionnotice_sent_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacatenotice',
            old_name='move_out_notice',
            new_name='move_out_date',
        ),
        migrations.AlterField(
            model_name='evictionnotice',
            name='notice_detail',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='vacatenotice',
            name='reason',
            field=models.TextField(max_length=1500),
        ),
    ]
