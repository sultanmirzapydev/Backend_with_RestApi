# Generated by Django 3.2.1 on 2021-07-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0016_remove_animal_likedcount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='total_liked',
            new_name='total_likd',
        ),
    ]
