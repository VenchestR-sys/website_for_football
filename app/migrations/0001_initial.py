# Generated by Django 5.1.5 on 2025-02-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('played', models.CharField(max_length=25)),
                ('won', models.CharField(max_length=255)),
                ('drawn', models.CharField(max_length=255)),
                ('lost', models.CharField(max_length=255)),
                ('against', models.CharField(max_length=255)),
                ('goal_difference', models.CharField(max_length=255)),
                ('points', models.CharField(max_length=255)),
                ('is_published', models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0)),
            ],
        ),
    ]
