# Generated by Django 2.2 on 2020-08-24 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20200824_0428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_id', to='webapp.Project', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='project', max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Описание'),
        ),
    ]