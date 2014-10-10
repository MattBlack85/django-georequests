# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('country', models.CharField(default=b'', max_length=25, blank=True)),
                ('url', models.CharField(max_length=100, verbose_name=b'requested url')),
                ('referer', models.CharField(default=b'', max_length=100, blank=True)),
                ('agent', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
