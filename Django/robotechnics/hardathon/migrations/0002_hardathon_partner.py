# Generated by Django 4.2.6 on 2023-10-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
        ('hardathon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardathon',
            name='partner',
            field=models.ManyToManyField(to='partners.partner', verbose_name='партнёры хардатона'),
        ),
    ]
