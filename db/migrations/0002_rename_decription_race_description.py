# Generated by Django 4.0.2 on 2024-11-05 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race',
            old_name='decription',
            new_name='description',
        ),
    ]
