# Generated by Django 4.2.3 on 2023-09-26 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_delete_sharedpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='no_of_shares',
        ),
    ]
