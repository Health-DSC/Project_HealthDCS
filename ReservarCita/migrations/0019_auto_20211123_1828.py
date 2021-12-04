# Generated by Django 3.2.9 on 2021-11-23 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservarCita', '0018_auto_20211123_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedenteAlergico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteFamiliar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(choices=[(1, 'Primer grado'), (2, 'Segundo grado'), (3, 'Tercer grado')], default='', max_length=19)),
                ('descripcion', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitos', models.CharField(default='', max_length=300)),
                ('medicamentos', models.CharField(default='', max_length=300)),
                ('transfunciones', models.CharField(default='', max_length=300)),
                ('patologias', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Triaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField(default=0)),
                ('talla', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='antecedente_alergico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ReservarCita.antecedentealergico'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='antecedente_familiar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ReservarCita.antecedentefamiliar'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='antecedente_general',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ReservarCita.antecedentegeneral'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='triaje',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ReservarCita.triaje'),
        ),
    ]
