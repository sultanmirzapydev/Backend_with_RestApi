# Generated by Django 3.2.1 on 2021-07-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_auto_20210703_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='isLiked',
            field=models.BooleanField(default=False, null=True),
        ),
    ]