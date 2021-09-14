# Generated by Django 3.2.6 on 2021-09-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title1_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название видео 1'),
        ),
        migrations.AddField(
            model_name='video',
            name='title1_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Название видео 1'),
        ),
        migrations.AddField(
            model_name='video',
            name='title2_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название видео 2'),
        ),
        migrations.AddField(
            model_name='video',
            name='title2_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Название видео 2'),
        ),
        migrations.AddField(
            model_name='video',
            name='title3_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название видео 3'),
        ),
        migrations.AddField(
            model_name='video',
            name='title3_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Название видео 3'),
        ),
        migrations.AddField(
            model_name='video',
            name='title4_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название видео 4'),
        ),
        migrations.AddField(
            model_name='video',
            name='title4_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Название видео 4'),
        ),
    ]
