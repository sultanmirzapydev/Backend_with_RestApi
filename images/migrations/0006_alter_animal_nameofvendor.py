# Generated by Django 3.2.1 on 2021-07-02 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20210702_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='nameOfVendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='theOneVendor', to='images.vendorname'),
        ),
    ]
