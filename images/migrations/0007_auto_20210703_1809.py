# Generated by Django 3.2.1 on 2021-07-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20210703_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='dd',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='df',
            field=models.IntegerField(null=True),
        ),
    ]
