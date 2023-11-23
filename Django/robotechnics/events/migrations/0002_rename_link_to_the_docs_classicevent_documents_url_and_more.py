# Generated by Django 4.2.6 on 2023-11-12 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classicevent',
            old_name='link_to_the_docs',
            new_name='documents_url',
        ),
        migrations.RenameField(
            model_name='classicevent',
            old_name='date_of_the_event',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='classicevent',
            old_name='venue',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='classicevent',
            old_name='link_to_photo_album',
            new_name='photo_album_url',
        ),
        migrations.RenameField(
            model_name='classicevent',
            old_name='link_to_the_registr',
            new_name='registration_link',
        ),
        migrations.RenameField(
            model_name='classicevent',
            old_name='mention_in_the_media',
            new_name='social_media_mention',
        ),
    ]
