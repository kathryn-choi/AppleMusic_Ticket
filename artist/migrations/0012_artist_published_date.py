# Generated by Django 2.0.6 on 2018-06-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0011_auto_20180614_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
