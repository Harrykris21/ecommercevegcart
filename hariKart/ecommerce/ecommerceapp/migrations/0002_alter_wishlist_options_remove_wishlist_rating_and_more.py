# Generated by Django 4.2 on 2023-09-21 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name_plural': 'Wish List'},
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='review',
        ),
    ]
