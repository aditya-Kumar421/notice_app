# Generated by Django 5.0.6 on 2024-06-04 14:04

import cloudinary.models
import notice.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, validators=[notice.models.validate_file_size]),
        ),
    ]
