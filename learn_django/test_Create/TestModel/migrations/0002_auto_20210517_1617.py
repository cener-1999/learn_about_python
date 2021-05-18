# Generated by Django 3.2.3 on 2021-05-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deathstatistics',
            name='date',
            field=models.CharField(max_length=30, unique=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='injuredstatistics',
            name='date',
            field=models.CharField(max_length=30, unique=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='missingstatistics',
            name='date',
            field=models.CharField(max_length=30, unique=True, verbose_name='日期'),
        ),
    ]
