# Generated by Django 3.0.5 on 2020-04-10 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(to='main_app.Photo'),
        ),
    ]
