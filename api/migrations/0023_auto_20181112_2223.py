# Generated by Django 2.1.1 on 2018-11-12 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20181112_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stylist',
            name='stylist',
        ),
        migrations.AlterField(
            model_name='stylist',
            name='image',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Image'),
        ),
    ]
