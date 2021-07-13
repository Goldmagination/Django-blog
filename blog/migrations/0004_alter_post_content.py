# Generated by Django 3.2.4 on 2021-07-13 14:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210713_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
