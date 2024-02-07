# Generated by Django 4.2.9 on 2024-01-23 07:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_delete_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_category',
            name='blog_summary',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog_category',
            name='blog_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
