# Generated by Django 5.0.3 on 2024-03-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addroom',
            name='image',
            field=models.FileField(default=True, null=True, upload_to='upload'),
        ),
    ]
