# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('milestones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='watchers',
            field=models.ManyToManyField(related_name='milestones_milestone+', to=settings.AUTH_USER_MODEL, verbose_name='watchers'),
        ),
    ]
