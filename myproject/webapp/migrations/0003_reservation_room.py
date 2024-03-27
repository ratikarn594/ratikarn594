# Generated by Django 5.0.3 on 2024-03-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_addroom_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomm', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.TimeField()),
                ('reservation_timestop', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=50)),
            ],
        ),
    ]
