# Generated by Django 3.0 on 2021-07-07 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20210707_0526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='article',
        ),
        migrations.AddField(
            model_name='user',
            name='article',
            field=models.ManyToManyField(to='school.Article'),
        ),
    ]
