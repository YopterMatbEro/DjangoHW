# Generated by Django 4.2.3 on 2023-08-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=64, null=True, verbose_name='Slug'),
        ),
    ]
