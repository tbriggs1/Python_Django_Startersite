# Generated by Django 3.0.6 on 2020-05-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20200521_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100)),
                ('floor_number', models.IntegerField(default=1)),
                ('room_number', models.IntegerField(default=1)),
            ],
        ),
    ]
