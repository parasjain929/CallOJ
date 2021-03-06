# Generated by Django 2.1 on 2020-05-24 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemLink', models.CharField(max_length=100)),
                ('problemName', models.CharField(max_length=100)),
                ('contestName', models.CharField(max_length=100)),
                ('difficultyLevel', models.IntegerField()),
                ('problemOfUser', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
