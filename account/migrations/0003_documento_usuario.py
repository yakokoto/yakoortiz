# Generated by Django 3.2.12 on 2022-08-04 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_is_recepcionista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('abogado', models.CharField(max_length=100)),
                ('comentarios', models.CharField(max_length=100)),
                ('fechaen', models.DateField(default=datetime.date.today)),
                ('fechaven', models.DateField(default=datetime.date(2022, 8, 19))),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=100)),
            ],
        ),
    ]
