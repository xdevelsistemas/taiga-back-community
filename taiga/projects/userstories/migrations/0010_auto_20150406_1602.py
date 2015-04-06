# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0009_remove_userstory_is_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='watchers',
            field=models.ManyToManyField(related_name='userstories_userstory+', to=settings.AUTH_USER_MODEL, verbose_name='watchers'),
        ),
    ]
