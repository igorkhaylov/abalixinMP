# Generated by Django 3.2.6 on 2021-09-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210924_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcasts',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='podcasts',
            name='description_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
