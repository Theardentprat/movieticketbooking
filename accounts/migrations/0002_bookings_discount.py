# Generated by Django 4.2.4 on 2023-08-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='discount',
            field=models.BooleanField(default=False),
        ),
    ]
