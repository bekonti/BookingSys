# Generated by Django 2.2.6 on 2019-10-27 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('city_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_info', models.TextField()),
                ('hotel_capacity', models.CharField(max_length=10)),
                ('hotel_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.City')),
            ],
        ),
    ]
