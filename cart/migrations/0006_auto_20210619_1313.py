# Generated by Django 3.2.3 on 2021-06-19 13:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20210619_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='percent',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='mart',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.mart'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo',
            field=models.CharField(max_length=50),
        ),
    ]
