# Generated by Django 3.2.1 on 2021-06-28 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='isLiked',
            new_name='liked',
        ),
        migrations.RenameField(
            model_name='typeof',
            old_name='breedName',
            new_name='animalType',
        ),
    ]
