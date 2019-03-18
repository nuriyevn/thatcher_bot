# Generated by Django 2.1.7 on 2019-03-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0002_auto_20190318_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.CharField(default='default', max_length=256),
        ),
        migrations.AddField(
            model_name='dish',
            name='type',
            field=models.CharField(default='default', max_length=256),
        ),
        migrations.AddField(
            model_name='set',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
