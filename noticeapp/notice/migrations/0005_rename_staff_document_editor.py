# Generated by Django 5.0.6 on 2024-06-05 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_remove_document_file_url_document_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='staff',
            new_name='editor',
        ),
    ]
