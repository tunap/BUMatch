# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0002_auto_20170513_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favor',
            fields=[
                ('favor_key', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('favor_id', models.IntegerField()),
                ('favor_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gachi',
            fields=[
                ('gachi_key', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('gachi_id', models.IntegerField()),
                ('gachi_value', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='match',
            old_name='from_user_id',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='to_user_id',
            new_name='user_id_end',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_10',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_3',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_4',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_5',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_6',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_7',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_8',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favor_9',
        ),
        migrations.RemoveField(
            model_name='user',
            name='text',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.AddField(
            model_name='match',
            name='is_picked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='is_watched',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='user_id_stt',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
