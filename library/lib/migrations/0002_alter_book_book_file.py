# Generated by Django 4.0.3 on 2022-03-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
