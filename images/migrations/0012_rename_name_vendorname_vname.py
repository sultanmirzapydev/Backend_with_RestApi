# Generated by Django 3.2.1 on 2021-07-02 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_auto_20210702_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorname',
            old_name='name',
            new_name='vname',
        ),
    ]