# Generated by Django 3.0.5 on 2021-04-01 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id']},
        ),
    ]
