# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-09 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stairdb', '0003_auto_20171109_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stair',
            name='handrail',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='N/A', max_length=25, null=True),
        ),
    ]
