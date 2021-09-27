# Generated by Django 3.2.6 on 2021-09-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_mainblock_podcast'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='description_ru',
            field=models.TextField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='categories',
            name='description_uz',
            field=models.TextField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='podcasts',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='podcasts',
            name='author_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='podcasts',
            name='author_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='podcasts',
            name='file',
            field=models.FileField(blank=True, upload_to='podcasts_audio/', verbose_name='Аудио файл'),
        ),
    ]
