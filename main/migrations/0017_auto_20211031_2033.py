# Generated by Django 3.2.6 on 2021-10-31 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210927_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-id'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='worldnews',
            options={'ordering': ['-date_created'], 'verbose_name': 'Мировые Новости', 'verbose_name_plural': 'Мировые новости'},
        ),
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_news', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='main_news', to='main.uzbnews', verbose_name='Главная новость')),
            ],
        ),
    ]