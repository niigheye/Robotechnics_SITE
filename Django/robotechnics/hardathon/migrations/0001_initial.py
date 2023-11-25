# Generated by Django 4.2.6 on 2023-11-25 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='изображение к мероприятию')),
                ('title', models.CharField(help_text='Максимум 150 символов', max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('photo_album_url', models.URLField(verbose_name='ссылка на фото-альбом')),
                ('documents_url', models.URLField(verbose_name='ссылка на документы')),
                ('location', models.URLField(verbose_name='место проведения')),
                ('event_date', models.DateField(verbose_name='дата проведения')),
                ('social_media_mention', models.URLField(verbose_name='упоминание в сми')),
                ('application_start_date', models.DateField(verbose_name='дата начала приёма заявок')),
                ('application_end_date', models.DateField(verbose_name='дата окончания приёма заявок')),
                ('date_of_summing_up', models.DateField(verbose_name='дата подведения итогов')),
                ('organizers_photo', models.ImageField(blank=True, upload_to='organizers_photos/%Y/%m/%d', verbose_name='фотография главного организатора')),
                ('organizers_word', models.URLField(verbose_name='слово главного организатора')),
                ('link_to_competition_task', models.URLField(verbose_name='ссылка на конкурсное задание')),
                ('partners', models.ManyToManyField(to='partners.partner', verbose_name='партнёры хардатона')),
            ],
            options={
                'verbose_name': 'хардатон',
                'verbose_name_plural': 'хардатоны',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='изображение к мероприятию')),
                ('title', models.CharField(help_text='Максимум 150 символов', max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('competition_rules', models.TextField(verbose_name='правила соревнования')),
                ('implementation_scale', models.TextField(verbose_name='масштаб реализации')),
                ('hardathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardathon.hardathon', verbose_name='хардатон')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
    ]
