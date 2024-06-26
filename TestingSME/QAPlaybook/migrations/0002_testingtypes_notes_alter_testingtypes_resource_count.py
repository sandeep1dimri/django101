# Generated by Django 5.0.4 on 2024-05-01 15:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QAPlaybook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testingtypes',
            name='notes',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='testingtypes',
            name='resource_count',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(10)]),
        ),
    ]
