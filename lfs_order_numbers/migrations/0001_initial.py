# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderNumberGenerator',
            fields=[
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('last', models.IntegerField(default=0, verbose_name='Last Order Number')),
                ('format', models.CharField(max_length=20, verbose_name='Format', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
