# Generated by Django 4.0.3 on 2022-03-20 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0002_alter_book_book_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageOfBoock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_file', models.FileField(blank=True, null=True, upload_to='pages/')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.AddField(
            model_name='book',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lib.pageofboock'),
            preserve_default=False,
        ),
    ]