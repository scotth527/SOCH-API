# Generated by Django 2.1.1 on 2018-11-20 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stylists', '0003_auto_20181120_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stylists.Stylist'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.ManyToManyField(blank=True, to='images.Image'),
        ),
    ]