# Generated by Django 4.2.2 on 2023-07-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todoapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dates', models.DateTimeField()),
                ('Importancy', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=100)),
            ],
        ),
    ]
