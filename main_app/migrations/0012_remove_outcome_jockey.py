# Generated by Django 3.1.6 on 2021-02-05 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20210205_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outcome',
            name='jockey',
        ),
    ]
