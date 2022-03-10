# Generated by Django 4.0.2 on 2022-03-08 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0061_waterpayments_lock'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitrentdetails',
            name='rent_type',
            field=models.CharField(choices=[('rent', 'Rent'), ('s_deposit', 'Security Deposit')], default='rent', max_length=15),
        ),
        migrations.AlterField(
            model_name='rentpayment',
            name='rent_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilities_and_rent.unitrentdetails'),
        ),
        migrations.AlterField(
            model_name='unitrentdetails',
            name='status',
            field=models.CharField(choices=[('unconfirmed', 'UnConfirmed'), ('refunded', 'Refunded'), ('rejected', 'Rejected'), ('confirmed', 'Confirmed')], default='unconfirmed', max_length=15),
        ),
    ]