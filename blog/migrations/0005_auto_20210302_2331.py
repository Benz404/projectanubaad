# Generated by Django 3.1.4 on 2021-03-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210302_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author_address',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author_mail',
            field=models.CharField(default='', max_length=50),
        ),
    ]