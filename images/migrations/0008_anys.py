# Generated by Django 3.2.1 on 2021-06-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_auto_20210629_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='anys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aa', models.CharField(max_length=10)),
            ],
        ),
    ]
