# Generated by Django 2.1.1 on 2018-11-12 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20181112_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Image'),
        ),
    ]
