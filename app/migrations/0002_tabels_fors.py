# Generated by Django 5.1.5 on 2025-02-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabels',
            name='fors',
            field=models.CharField(default='default_value', max_length=255),
        ),
    ]
