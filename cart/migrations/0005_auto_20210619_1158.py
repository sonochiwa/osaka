# Generated by Django 3.2.3 on 2021-06-19 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20210619_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='index',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='mart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.mart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='promo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
