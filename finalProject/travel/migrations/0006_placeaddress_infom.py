# Generated by Django 2.2.5 on 2021-05-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_placeaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeaddress',
            name='infom',
            field=models.CharField(default='无', max_length=255),
        ),
    ]
