# Generated by Django 2.1 on 2018-08-17 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dresses', '0002_auto_20180817_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lehengas',
            name='lehenga_price',
        ),
    ]
