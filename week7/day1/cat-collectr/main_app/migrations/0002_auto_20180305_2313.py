# Generated by Django 2.0.2 on 2018-03-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.IntegerField(),
        ),
    ]
