# Generated by Django 4.2.7 on 2023-12-21 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPP', '0004_rename_author_post_autor_rename_date_post_fecha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='texto',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='fecha',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='subtitulo',
            new_name='subtitle',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
    ]
