# Generated by Django 4.2.4 on 2023-09-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_bookings_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='uads',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
