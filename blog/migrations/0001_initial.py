# Generated by Django 3.1.4 on 2021-02-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('contant1', models.CharField(default='', max_length=50000)),
                ('image1', models.ImageField(upload_to='')),
                ('contant2', models.CharField(default='', max_length=50000)),
                ('image2', models.ImageField(upload_to='')),
                ('contant3', models.CharField(default='', max_length=50000)),
                ('date_time', models.DateField()),
            ],
        ),
    ]
