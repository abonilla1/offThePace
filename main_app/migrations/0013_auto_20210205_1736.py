# Generated by Django 3.1.6 on 2021-02-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_outcome_jockey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='outcome',
            field=models.CharField(choices=[('W', 'Win'), ('P', 'Place'), ('S', 'Show'), ('U', 'Unplaced')], default='W', max_length=1),
        ),
    ]
