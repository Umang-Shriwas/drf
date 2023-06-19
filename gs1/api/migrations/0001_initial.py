# Generated by Django 3.1.8 on 2023-06-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
