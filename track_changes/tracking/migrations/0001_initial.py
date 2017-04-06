# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('CR', 'Created'), ('RE', 'Retrieved'), ('UP', 'Updated'), ('DE', 'Deleted')], max_length=2)),
                ('changed_fields', models.CharField(max_length=1024)),
                ('changed_data', models.CharField(max_length=1024)),
                ('changed_pk', models.BigIntegerField()),
                ('changed_class', models.CharField(max_length=128)),
                ('time_changed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
