# Generated by Django 2.2 on 2020-08-10 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200810_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='type',
            new_name='types',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='status',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='type',
            new_name='name',
        ),
    ]