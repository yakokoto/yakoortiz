# Generated by Django 4.1.2 on 2022-10-26 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_contrasena'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='expediente',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='documento',
            name='fechaven',
            field=models.DateField(default=datetime.date(2022, 11, 10)),
        ),
    ]
