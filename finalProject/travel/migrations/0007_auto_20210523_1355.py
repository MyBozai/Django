# Generated by Django 2.2.5 on 2021-05-23 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_placeaddress_infom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeaddress',
            name='infom',
            field=models.CharField(default='无', max_length=5000),
        ),
    ]