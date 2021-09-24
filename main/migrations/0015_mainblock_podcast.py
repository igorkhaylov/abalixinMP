# Generated by Django 3.2.6 on 2021-09-24 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210924_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainblock',
            name='podcast',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='podcast', to='main.podcasts', verbose_name='Подкаст'),
            preserve_default=False,
        ),
    ]
