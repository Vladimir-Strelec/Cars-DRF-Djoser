# Generated by Django 4.0.4 on 2022-05-27 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_car', '0002_carmodel_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='created',
            new_name='owner',
        ),
    ]
