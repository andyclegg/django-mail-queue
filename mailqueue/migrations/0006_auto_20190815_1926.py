# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-15 19:26
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import mailqueue.utils


class Migration(migrations.Migration):

    dependencies = [
        ('mailqueue', '0005_cc_address_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file_attachment',
            field=models.FileField(blank=True, null=True,
                                   storage=django.core.files.storage.FileSystemStorage(location=''),
                                   upload_to=mailqueue.utils.upload_to),
        ),
    ]
