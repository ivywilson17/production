# Generated by Django 4.1.7 on 2023-03-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0003_rename_desg_movie_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hello', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
