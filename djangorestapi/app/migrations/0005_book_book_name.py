# Generated by Django 3.2.3 on 2021-05-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_name',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
    ]
