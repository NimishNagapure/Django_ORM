# Generated by Django 3.0 on 2021-07-07 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20210707_1031'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Userd',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='arti',
            new_name='article',
        ),
    ]
