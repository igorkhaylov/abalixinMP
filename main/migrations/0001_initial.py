# Generated by Django 3.2.6 on 2021-09-06 16:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(max_length=120, verbose_name='Короткое название')),
                ('short_title_ru', models.CharField(max_length=120, null=True, verbose_name='Короткое название')),
                ('short_title_uz', models.CharField(max_length=120, null=True, verbose_name='Короткое название')),
                ('title', models.CharField(max_length=250, verbose_name='Название статьи')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Название статьи')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='Название статьи')),
                ('title1', models.CharField(max_length=120, verbose_name='Короткое название 1')),
                ('title1_ru', models.CharField(max_length=120, null=True, verbose_name='Короткое название 1')),
                ('title1_uz', models.CharField(max_length=120, null=True, verbose_name='Короткое название 1')),
                ('title2', models.CharField(max_length=120, verbose_name='Короткое название 2')),
                ('title2_ru', models.CharField(max_length=120, null=True, verbose_name='Короткое название 2')),
                ('title2_uz', models.CharField(max_length=120, null=True, verbose_name='Короткое название 2')),
                ('image', models.ImageField(upload_to='article/%Y/%m/%d/', verbose_name='Картинка')),
                ('slug', models.SlugField(max_length=120, unique=True, verbose_name='Slug')),
                ('short_description', models.TextField(max_length=300, verbose_name='Короткое описание')),
                ('short_description_ru', models.TextField(max_length=300, null=True, verbose_name='Короткое описание')),
                ('short_description_uz', models.TextField(max_length=300, null=True, verbose_name='Короткое описание')),
                ('description', models.TextField(verbose_name='Описание статьи')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание статьи')),
                ('description_uz', models.TextField(null=True, verbose_name='Описание статьи')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('name_ru', models.CharField(max_length=120, null=True, verbose_name='Имя')),
                ('name_uz', models.CharField(max_length=120, null=True, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_uz', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название категории')),
                ('name_ru', models.CharField(max_length=120, null=True, verbose_name='Название категории')),
                ('name_uz', models.CharField(max_length=120, null=True, verbose_name='Название категории')),
                ('url', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=250, verbose_name='Название статьи')),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Бегущая строка', editable=False, max_length=120, verbose_name='Бегущая строка')),
                ('ticker', models.CharField(max_length=500, verbose_name='Бегущая строка')),
                ('ticker_ru', models.CharField(max_length=500, null=True, verbose_name='Бегущая строка')),
                ('ticker_uz', models.CharField(max_length=500, null=True, verbose_name='Бегущая строка')),
            ],
            options={
                'verbose_name': 'Бегущая строка',
                'verbose_name_plural': 'Бегущая строка',
            },
        ),
        migrations.CreateModel(
            name='MainBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article1', to='main.articles', verbose_name='Статья 1')),
                ('article2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article2', to='main.articles', verbose_name='Статья 2')),
                ('article3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article3', to='main.articles', verbose_name='Статья 3')),
                ('article4', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article4', to='main.articles', verbose_name='Статья 4')),
                ('article5', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article5', to='main.articles', verbose_name='Статья 5')),
                ('article6', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article6', to='main.articles', verbose_name='Статья 6')),
                ('firstArticle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='firstArticle', to='main.articles', verbose_name='Первая статья')),
                ('secondArticle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='secondArticle', to='main.articles', verbose_name='Вторая статья')),
                ('thirdArticle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='thirdArticle', to='main.articles', verbose_name='Третья статья')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to='main.author', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='articles',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main.categories', verbose_name='Категории'),
        ),
    ]