# Generated by Django 3.0.5 on 2021-03-25 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20210326_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='description',
        ),
    ]