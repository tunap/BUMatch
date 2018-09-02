# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=10)),
                ('user_my_gender', models.IntegerField()),
                ('user_ur_gender', models.IntegerField()),
                ('user_description', models.CharField(max_length=20)),
                ('user_login_id', models.CharField(max_length=20)),
                ('user_login_pw', models.CharField(max_length=20)),
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
        migrations.DeleteModel(
            name='Users',
        ),
    ]
