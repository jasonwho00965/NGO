# Generated by Django 2.1.7 on 2019-04-01 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190401_1636'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='EventManagement',
        ),
        migrations.RenameModel(
            old_name='User_Management',
            new_name='UserManagement',
        ),
    ]
