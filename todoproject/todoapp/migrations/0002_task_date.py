# Generated by Django 4.2.5 on 2023-09-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-04-25'),
            preserve_default=False,
        ),
    ]
