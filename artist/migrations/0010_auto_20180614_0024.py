# Generated by Django 2.0.6 on 2018-06-14 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0009_auto_20180614_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
