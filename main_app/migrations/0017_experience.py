# Generated by Django 3.1.6 on 2021-02-05 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20210205_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Race Title', max_length=150)),
                ('date', models.DateField(verbose_name='Date')),
                ('experience', models.CharField(choices=[('W', 'Win'), ('P', 'Place'), ('S', 'Show'), ('U', 'Unplaced')], default='W', max_length=1)),
                ('jockey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.jockey')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]