# Generated by Django 5.0 on 2023-12-08 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='use',
            new_name='user',
        ),
    ]
