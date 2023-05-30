# Generated by Django 4.1.9 on 2023-05-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('reparto', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Persone',
            },
        ),
    ]