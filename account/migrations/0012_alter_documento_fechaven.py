# Generated by Django 4.1.2 on 2022-11-08 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_contrasena_rfc_alter_firma_rfc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='fechaven',
            field=models.DateField(default=datetime.date(2022, 11, 23)),
        ),
    ]