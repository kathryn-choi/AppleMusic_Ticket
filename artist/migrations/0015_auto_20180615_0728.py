# Generated by Django 2.0.6 on 2018-06-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0014_auto_20180615_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
