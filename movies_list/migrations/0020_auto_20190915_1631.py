# Generated by Django 2.2 on 2019-09-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0019_auto_20190915_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
