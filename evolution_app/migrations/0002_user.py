# Generated by Django 3.0.3 on 2020-06-28 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evolution_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264, unique=True)),
                ('last_name', models.CharField(max_length=264, unique=True)),
                ('username', models.CharField(max_length=264, unique=True)),
                ('email', models.CharField(max_length=264, unique=True)),
                ('password', models.CharField(max_length=264, unique=True)),
                ('address', models.CharField(max_length=264, unique=True)),
                ('phone', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
