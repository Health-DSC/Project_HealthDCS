# Generated by Django 3.2.9 on 2021-11-21 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservarCita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilitado', models.BooleanField(default=1)),
            ],
        ),
    ]
