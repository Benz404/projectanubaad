# Generated by Django 3.1.4 on 2021-03-02 17:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogpost_main_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='contant',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
