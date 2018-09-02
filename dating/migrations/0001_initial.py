# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('from_user_id', models.IntegerField()),
                ('to_user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=10)),
                ('user_gender', models.IntegerField()),
                ('favor_1', models.IntegerField()),
                ('favor_2', models.IntegerField()),
                ('favor_3', models.IntegerField()),
                ('favor_4', models.IntegerField()),
                ('favor_5', models.IntegerField()),
                ('favor_6', models.IntegerField()),
                ('favor_7', models.IntegerField()),
                ('favor_8', models.IntegerField()),
                ('favor_9', models.IntegerField()),
                ('favor_10', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
