# Generated by Django 2.1.1 on 2018-11-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20181119_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchased',
            name='products',
            field=models.ManyToManyField(blank=True, default='', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='purchased',
            name='styles',
            field=models.ManyToManyField(blank=True, default='', to='styles.Style'),
        ),
    ]
