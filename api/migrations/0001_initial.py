# Generated by Django 4.2.2 on 2023-06-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('date1', models.CharField(max_length=5)),
                ('date2', models.CharField(max_length=5)),
                ('date3', models.CharField(max_length=5)),
                ('date4', models.CharField(max_length=5)),
            ],
        ),
    ]