# Generated by Django 2.1 on 2020-05-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemCode', models.CharField(max_length=50)),
                ('problemName', models.CharField(max_length=100)),
                ('problemStatement', models.TextField()),
                ('timeLimit', models.FloatField()),
                ('memoryLimit', models.IntegerField()),
                ('creator', models.CharField(max_length=20)),
                ('editorialist', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemCode', models.CharField(max_length=50)),
                ('problemName', models.CharField(max_length=100)),
                ('problemStatement', models.TextField()),
                ('timeLimit', models.FloatField()),
                ('memoryLimit', models.IntegerField()),
                ('marking', models.IntegerField()),
                ('access', models.IntegerField()),
                ('creator', models.CharField(max_length=20)),
                ('editorialist', models.CharField(max_length=20)),
                ('totalAttempts', models.IntegerField()),
                ('successfulAttempts', models.IntegerField()),
            ],
        ),
    ]
