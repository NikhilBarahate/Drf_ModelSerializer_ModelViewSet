# Generated by Django 4.0.3 on 2022-03-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('rn', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('addr', models.CharField(max_length=200)),
                ('marks', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
