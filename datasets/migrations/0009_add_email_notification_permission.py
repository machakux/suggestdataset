# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-28 11:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0008_add_field_dataset_is_public'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataset',
            options={'permissions': (('can_receive_new_suggestion_email', 'Can receive notification on new dataset suggestions'),), 'verbose_name': 'Dataset Suggestion', 'verbose_name_plural': 'Datasets Suggestions'},
        ),
    ]