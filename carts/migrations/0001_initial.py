# Generated by Django 2.1.1 on 2018-11-24 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased', models.BooleanField(default=False)),
                ('purchase_date', models.DateField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, default=25.0, max_digits=10)),
                ('tax_percentage', models.DecimalField(decimal_places=5, default=0.065, max_digits=10)),
                ('tax_total', models.DecimalField(decimal_places=2, default=25.0, max_digits=50)),
                ('total', models.DecimalField(decimal_places=2, default=25.0, max_digits=50)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Variation')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='carts.CartItem', to='products.Variation'),
        ),
    ]
