# Generated by Django 4.0.4 on 2022-06-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_alter_books_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(blank=True, upload_to='books'),
        ),
    ]
