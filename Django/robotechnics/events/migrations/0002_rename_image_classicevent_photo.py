# Generated by Django 4.2.6 on 2023-11-23 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classicevent',
            old_name='image',
            new_name='photo',
        ),
    ]
