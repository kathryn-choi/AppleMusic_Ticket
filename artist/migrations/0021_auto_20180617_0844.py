# Generated by Django 2.0.6 on 2018-06-17 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0020_post_ticketlink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='artist',
            new_name='artistname',
        ),
    ]
