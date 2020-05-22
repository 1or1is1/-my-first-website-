# Generated by Django 3.0.5 on 2020-05-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=50, unique=True)),
                ('movie_description', models.CharField(max_length=300, null=True)),
                ('movie_likes', models.IntegerField(default=0)),
                ('movie_dislikes', models.IntegerField(default=0)),
            ],
        ),
    ]