# Generated by Django 5.0.6 on 2024-05-26 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littleLemon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='price',
            new_name='fee',
        ),
    ]