# Generated by Django 3.1.6 on 2021-02-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20210205_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcome',
            name='name',
            field=models.CharField(default='name of race', max_length=150),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]