# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, to='students.Student', blank=True, null=True, verbose_name='Leader'),
        ),
    ]
