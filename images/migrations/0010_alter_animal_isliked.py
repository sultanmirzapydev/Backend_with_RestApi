# Generated by Django 3.2.1 on 2021-07-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_alter_animal_isliked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='isLiked',
            field=models.BooleanField(null=True),
        ),
    ]
