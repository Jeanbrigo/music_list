# Generated by Django 4.1.7 on 2023-02-21 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='Artist',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='Title',
            new_name='title',
        ),
    ]