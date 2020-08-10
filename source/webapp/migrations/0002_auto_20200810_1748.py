# Generated by Django 2.2 on 2020-08-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='type',
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='type_key', to='webapp.Type', verbose_name='Тип'),
        ),
    ]
