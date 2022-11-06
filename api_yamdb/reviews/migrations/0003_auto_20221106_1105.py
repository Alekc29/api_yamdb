# Generated by Django 2.2.16 on 2022-11-06 08:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221106_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='оценка'),
        ),
    ]