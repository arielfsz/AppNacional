# Generated by Django 4.1.2 on 2022-11-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Futbolista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('nacimiento', models.DateTimeField()),
                ('posicion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('año', models.IntegerField()),
                ('caracter', models.CharField(max_length=20)),
                ('nacionalidad', models.CharField(max_length=20)),
            ],
        ),
    ]
