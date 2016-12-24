# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 00:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import slugid.slugid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tileset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.CharField(default=slugid.slugid.nice, max_length=100, unique=True)),
                ('processed_file', models.TextField()),
                ('filetype', models.TextField()),
                ('datatype', models.TextField(default='unknown')),
                ('private', models.BooleanField(default=False)),
                ('name', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tilesets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
                'permissions': (('view_tileset', 'View tileset'),),
            },
        ),
    ]
