# Generated by Django 2.0.6 on 2018-06-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0024_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='albumname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='nameofsong',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='releasedate',
            field=models.CharField(max_length=30),
        ),
    ]