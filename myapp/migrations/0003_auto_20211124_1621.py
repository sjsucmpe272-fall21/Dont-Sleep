# Generated by Django 3.2.9 on 2021-11-25 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20211124_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='RefContactNo1',
            new_name='RefContactNo',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='RefName1',
            new_name='RefName',
        ),
    ]