# Generated by Django 3.2.1 on 2021-07-02 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_auto_20210702_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorname',
            name='typeOfVendorRef',
        ),
    ]