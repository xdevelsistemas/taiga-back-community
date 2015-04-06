# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20141029_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historychangenotification',
            name='history_entries',
            field=models.ManyToManyField(related_name='+', to='history.HistoryEntry', verbose_name='history entries'),
        ),
        migrations.AlterField(
            model_name='historychangenotification',
            name='notify_users',
            field=models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='notify users'),
        ),
    ]
