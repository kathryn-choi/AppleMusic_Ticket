# Generated by Django 2.0.6 on 2018-06-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0022_auto_20180617_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='region',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
