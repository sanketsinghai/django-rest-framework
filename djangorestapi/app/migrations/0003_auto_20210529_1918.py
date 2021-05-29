# Generated by Django 3.2.3 on 2021-05-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_students_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=20, max_length=100),
            preserve_default=False,
        ),
    ]