# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-26 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0005_remove_field_is_open_issue_on_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='Archived'),
        ),
    ]