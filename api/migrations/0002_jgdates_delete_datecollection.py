# Generated by Django 4.2.2 on 2023-06-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JGdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True)),
                ('date1', models.CharField(max_length=5)),
                ('date2', models.CharField(max_length=5)),
                ('date3', models.CharField(max_length=5)),
                ('date4', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='DateCollection',
        ),
    ]