# Generated by Django 4.1.9 on 2023-05-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricevi', '0002_persona_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='password',
            field=models.CharField(default='password.123', max_length=50),
        ),
    ]
