# Generated by Django 3.2.9 on 2021-11-23 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservarCita', '0017_auto_20211122_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('FIE', 'Financiados íntegramente por el Estado'), ('FE', 'Financiados por el Estado'), ('FEA', 'Financiado por empleadores o afiliados')], default='', max_length=25)),
                ('aseguradora', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='aseguradora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ReservarCita.seguro'),
        ),
    ]
