# Generated by Django 2.2 on 2020-09-15 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_project_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('can_change_group', 'Изменяет состав группы')], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]