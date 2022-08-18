# Generated by Django 3.2.5 on 2021-07-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqljoin', '0003_article_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('books', models.ManyToManyField(to='sqljoin.Book')),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='best_pizza',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='pizzas',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
