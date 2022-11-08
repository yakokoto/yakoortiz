# Generated by Django 3.2.12 on 2022-09-06 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220829_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empresa', models.CharField(max_length=100)),
                ('fiel', models.FileField(upload_to='fiel/')),
                ('ciec', models.FileField(upload_to='ciec/')),
            ],
        ),
        migrations.AlterField(
            model_name='documento',
            name='fechaven',
            field=models.DateField(default=datetime.date(2022, 9, 21)),
        ),
        migrations.AlterField(
            model_name='provedor',
            name='correo',
            field=models.EmailField(max_length=100),
        ),
    ]
