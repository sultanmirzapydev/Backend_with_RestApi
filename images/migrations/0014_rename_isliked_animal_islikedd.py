# Generated by Django 3.2.1 on 2021-07-03 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0013_alter_animal_isliked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='isLiked',
            new_name='isLikedd',
        ),
    ]