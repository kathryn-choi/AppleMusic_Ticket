# Generated by Django 2.0.6 on 2018-06-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0019_auto_20180617_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ticketlink',
            field=models.URLField(default=''),
        ),
    ]