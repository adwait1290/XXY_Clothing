# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_cartitem_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='image_url',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', verbose_name=b'Image'),
        ),
    ]
