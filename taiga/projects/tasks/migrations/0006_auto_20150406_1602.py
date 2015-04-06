# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150114_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='watchers',
            field=models.ManyToManyField(related_name='tasks_task+', to=settings.AUTH_USER_MODEL, verbose_name='watchers'),
        ),
    ]
