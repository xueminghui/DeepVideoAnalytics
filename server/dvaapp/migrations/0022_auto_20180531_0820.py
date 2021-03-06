# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-31 08:20
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0021_auto_20180531_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='TubeRegionRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('weight', models.FloatField(null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Region')),
                ('tube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Tube')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video')),
            ],
        ),
        migrations.CreateModel(
            name='TubeRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('weight', models.FloatField(null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('source_tube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_tube', to='dvaapp.Tube')),
                ('target_tube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_tube', to='dvaapp.Tube')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video')),
            ],
        ),
        migrations.RemoveField(
            model_name='regionrelation',
            name='source_frame_index',
        ),
        migrations.RemoveField(
            model_name='regionrelation',
            name='source_segment_index',
        ),
        migrations.RemoveField(
            model_name='regionrelation',
            name='target_frame_index',
        ),
        migrations.RemoveField(
            model_name='regionrelation',
            name='target_segment_index',
        ),
    ]
