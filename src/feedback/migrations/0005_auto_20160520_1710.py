# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20160520_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='fbtype',
            new_name='type',
        ),
    ]