# Generated by Django 2.2.6 on 2019-11-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carRent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmod',
            name='amount',
            field=models.IntegerField(default=20),
        ),
    ]
