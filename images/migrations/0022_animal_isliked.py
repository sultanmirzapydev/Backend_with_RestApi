# Generated by Django 3.2.1 on 2021-07-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0021_auto_20210703_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='isLiked',
            field=models.BooleanField(default=False),
        ),
    ]