# Generated by Django 4.0.3 on 2022-03-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_alter_book_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageofboock',
            old_name='book_file',
            new_name='page_file',
        ),
    ]