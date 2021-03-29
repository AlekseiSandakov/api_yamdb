# Generated by Django 3.0.5 on 2021-03-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='category',
            field=models.ManyToManyField(blank=True, to='content.Category'),
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, to='content.Genre'),
        ),
    ]
