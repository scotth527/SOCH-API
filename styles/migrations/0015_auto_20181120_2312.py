# Generated by Django 2.1.1 on 2018-11-20 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0014_auto_20181120_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='image',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='images.Image'),
        ),
    ]