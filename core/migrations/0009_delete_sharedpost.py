# Generated by Django 4.2.3 on 2023-09-26 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_post_no_of_shares'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SharedPost',
        ),
    ]
