# Generated by Django 2.0.2 on 2018-05-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20180520_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(help_text="Enter the course's title number (220 in COMPSCI 220)", max_length=20),
        ),
    ]
