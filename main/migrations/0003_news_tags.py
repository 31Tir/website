# Generated by Django 3.0.1 on 2020-01-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200119_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.TextField(default='not specified'),
        ),
    ]
