# Generated by Django 2.2.1 on 2019-05-02 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190502_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectpage',
            old_name='participate',
            new_name='participants',
        ),
        migrations.RenameField(
            model_name='projectpage',
            old_name='users',
            new_name='waiting_list',
        ),
    ]