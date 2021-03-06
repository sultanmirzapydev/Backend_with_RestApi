# Generated by Django 3.2.1 on 2021-07-07 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalType', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='vendorName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('avatar', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('descriptions', models.TextField(null=True)),
                ('imgUrl', models.TextField(null=True)),
                ('count', models.IntegerField(null=True)),
                ('total_liked', models.IntegerField(null=True)),
                ('isLiked', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('offers', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('typeOf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='typeOf', to='images.typeof')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='images.vendorname')),
            ],
        ),
    ]
