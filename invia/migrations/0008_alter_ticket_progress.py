# Generated by Django 4.1.9 on 2023-05-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invia', '0007_alter_ticket_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='progress',
            field=models.CharField(default='Non Accettato', max_length=20),
        ),
    ]
