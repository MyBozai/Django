# Generated by Django 2.2.5 on 2021-05-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_user_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
