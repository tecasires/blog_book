# Generated by Django 4.0.4 on 2022-06-08 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_rename_isbn_books_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authors',
            old_name='day_birth',
            new_name='birthday',
        ),
    ]
