# Generated by Django 2.1.7 on 2019-04-01 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_event_e_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='e_category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='e_end_date',
            new_name='End_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='e_name',
            new_name='Event',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='e_location',
            new_name='Location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='e_start_date',
            new_name='Start_date',
        ),
    ]
