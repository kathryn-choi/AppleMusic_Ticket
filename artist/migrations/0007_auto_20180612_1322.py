# Generated by Django 2.0.6 on 2018-06-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0006_auto_20180612_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(default='illenium.jpeg', upload_to=''),
        ),
    ]
