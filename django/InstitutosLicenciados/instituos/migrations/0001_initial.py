# Generated by Django 4.2.1 on 2023-05-28 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutosConLicencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('personJuridica', models.CharField(max_length=100)),
                ('sedeLocal', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('programasLicenciados', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=50)),
                ('modalidad', models.CharField(max_length=20)),
            ],
        ),
    ]
