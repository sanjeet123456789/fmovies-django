# Generated by Django 2.2 on 2019-09-15 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0015_auto_20190914_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies_list',
            name='thumbnail',
            field=models.ImageField(default='thumbnail.jpg', upload_to='movies_pics'),
        ),
    ]
