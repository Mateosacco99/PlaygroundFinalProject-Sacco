# Generated by Django 4.2.7 on 2023-12-21 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPP', '0002_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagepost',
        ),
    ]
