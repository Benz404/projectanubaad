# Generated by Django 3.1.4 on 2021-03-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='date_time',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='contant1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='contant2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='contant3',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='image2',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='contant',
            field=models.TextField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='main_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
