# Generated by Django 3.2.9 on 2022-03-04 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_alter_order_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 15, 49, 15, 355551)),
        ),
    ]
