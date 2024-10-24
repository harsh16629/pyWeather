# Generated by Django 5.1.2 on 2024-10-22 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_searchhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='city',
            new_name='city_name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_posted',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='searchhistory',
            old_name='city',
            new_name='city_name',
        ),
        migrations.RenameField(
            model_name='searchhistory',
            old_name='timestamp',
            new_name='search_date',
        ),
    ]
