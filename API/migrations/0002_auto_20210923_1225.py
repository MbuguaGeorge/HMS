# Generated by Django 3.2.7 on 2021-09-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='identification',
            field=models.IntegerField(default=36827354, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=72835215, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
