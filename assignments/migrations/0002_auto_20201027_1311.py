# Generated by Django 3.1.1 on 2020-10-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='due_time',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
