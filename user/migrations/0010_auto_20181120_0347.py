# Generated by Django 2.1.1 on 2018-11-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20181119_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchased',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
