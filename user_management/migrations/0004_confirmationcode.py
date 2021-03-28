# Generated by Django 3.1.7 on 2021-03-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_auto_20210328_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_code', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('code_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
