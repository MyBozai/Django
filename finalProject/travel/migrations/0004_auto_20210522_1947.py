# Generated by Django 2.2.5 on 2021-05-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='place',
            field=models.CharField(max_length=50),
        ),
    ]