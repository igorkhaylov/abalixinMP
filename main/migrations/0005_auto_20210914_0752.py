# Generated by Django 3.2.6 on 2021-09-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210914_0740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uzbnews',
            options={'verbose_name': 'Новости Узбекистана', 'verbose_name_plural': 'Новости Узбекистана'},
        ),
        migrations.AlterModelOptions(
            name='worldnews',
            options={'verbose_name': 'Мировые Новости', 'verbose_name_plural': 'Мировые новости'},
        ),
        migrations.AddField(
            model_name='uzbnews',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='uzbnews',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='uzbnews',
            name='short_title_ru',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='uzbnews',
            name='short_title_uz',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='uzbnews',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название статьи'),
        ),
        migrations.AddField(
            model_name='uzbnews',
            name='title_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Название статьи'),
        ),
        migrations.AddField(
            model_name='worldnews',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='worldnews',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='worldnews',
            name='short_title_ru',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='worldnews',
            name='short_title_uz',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='worldnews',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название новости'),
        ),
        migrations.AddField(
            model_name='worldnews',
            name='title_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Название новости'),
        ),
    ]