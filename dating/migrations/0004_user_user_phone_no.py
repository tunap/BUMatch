# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0003_auto_20170513_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_phone_no',
            field=models.CharField(max_length=20, default=1),
            preserve_default=False,
        ),
    ]
