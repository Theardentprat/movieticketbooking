# Generated by Django 4.2.4 on 2023-09-02 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_bookings_uads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='uads',
        ),
    ]
