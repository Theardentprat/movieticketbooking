# Generated by Django 4.2.4 on 2023-08-13 09:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(default='cinema_manager', max_length=30)),
                ('cinema_name', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_trailer', models.URLField(max_length=300)),
                ('movie_rdate', models.DateField(auto_now=True)),
                ('movie_des', models.TextField()),
                ('movie_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('movie_poster', models.ImageField(default='movies/poster/not.jpg', upload_to='movies/poster')),
                ('movie_genre', models.CharField(default='Action | Comedy | Romance', max_length=50)),
                ('movie_duration', models.DurationField(default=datetime.timedelta(seconds=9900))),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('shows', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(default=django.utils.timezone.now, max_length=15)),
                ('price', models.IntegerField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_show', to='accounts.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_show', to='accounts.movie')),
            ],
            options={
                'verbose_name_plural': 'Shows',
            },
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useat', models.CharField(max_length=100)),
                ('shows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.shows')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
