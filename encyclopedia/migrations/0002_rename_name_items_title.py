# Generated by Django 3.2.1 on 2021-05-15 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='name',
            new_name='title',
        ),
    ]