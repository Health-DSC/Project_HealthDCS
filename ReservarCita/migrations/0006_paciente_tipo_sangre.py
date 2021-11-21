# Generated by Django 3.2.9 on 2021-11-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservarCita', '0005_alter_paciente_id_seguro'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='tipo_sangre',
            field=models.CharField(choices=[('-A', '-A'), ('B', 'B'), ('O', 'O'), ('ABO', 'ABO')], default='O', max_length=3),
        ),
    ]
