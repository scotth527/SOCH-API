# Generated by Django 2.1.1 on 2018-11-26 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
