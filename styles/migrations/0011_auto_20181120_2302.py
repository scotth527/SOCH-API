# Generated by Django 2.1.1 on 2018-11-20 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0010_auto_20181120_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='image',
            field=models.OneToOneField(default={}, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.Image'),
        ),
    ]